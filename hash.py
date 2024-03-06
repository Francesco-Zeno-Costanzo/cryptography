"""
Code to compute hash with 256 bits
"""
from hash_constant import *

#==========================================================================================
# Function useful in the translation
#==========================================================================================

def translate(msg):
    '''
    Function to translate message in bits

    Parameters
    ----------
    msg : string
        message to translate

    Returns
    -------
    bits : list
        list of bit rappresentation of msg
    '''
    # Trasform in Unicode values the in binary rappresentation
    char_codes = [ord(m) for m in msg]
    bytes = []
    for c in char_codes:
        bytes.append(bin(c)[2:].zfill(8))

    # From a list of number to a list with splitted values
    # e.g. [11, 01] -> [1, 1, 0, 1]
    bits = []
    for byte in bytes:
        for bit in byte:
            bits.append(int(bit))

    return bits


def init(number):
    '''
    Function to initialize NIST's constant

    Parameters
    ----------
    number : list
        list of strings in hexadecimal format

    Returns
    -------
    result : list
        list of list, each inner list contains the binary
        rappresentation of the element of number
    '''
    # Convert values in base 16 and then in binary
    # [2:] is to delete the '0b' part
    binaries = [bin(int(v, 16))[2:] for v in number]
    result   = []
    # Split all number in a list and pad with zeros
    # to obtain the same length for all numbers (32 bits)
    for binary in binaries:
        w = []
        for b in binary:
            w.append(int(b))
        result.append(pad_zero(w, 32, 'start'))
    return result


def pad_zero(bits, length, loc='end'):
    '''
    Function to add zero to obtain binary number with equal size

    Parameters
    ----------
    bits : list
        ...
    length : int
        length of the returned list
    loc : string, optional, default 'end'
        location where append the zeros

    Returns
    -------
    bits : list
        padded list
    '''
    l = len(bits)
    # Pad at the end of number
    if loc == 'end':
        for i in range(l, length):
            bits.append(0)
    # Pad at the start of number (simeq .zfill)
    if loc == 'start':
        while l < length:
            bits.insert(0, 0)
            l = len(bits)

    return bits


def chunker(bits, l):
    '''
    Function to divides list of bits into byte chunks,

    Parameters
    ----------
    bits : list
        list of bits
    l : int
        size of the chunk

    Returns
    -------
    chunck : list
        list of list, each inner list is a part of bits of length l
    '''
    chunk = []
    for b in range(0, len(bits), l):
        chunk.append(bits[b : b + l])
    return chunk


def pre_process(msg):
    '''
    Function to pre process message to compute the hash

    Parameters
    ----------
    msg : string
        message to translate

    Returns
    -------
    bits : list
        pre processed list of bit rappresentation of msg
    '''
    # translate message into bits
    bits  = translate(msg)
    L     = len(bits)
    L_bit = [int(b) for b in bin(L)[2:].zfill(64)] # L in bit

    # if L < 448 put 1 at the end
    # Padd
    # Add the 64 bits representing the length of the message
    if L < 448:
        bits.append(1)
        bits = pad_zero(bits, 448, 'end')
        bits = bits + L_bit
        return [bits]

    # If 448 <= L <= 512 bits, put 1 at end, we go to the next multiple of 512 (i.e. 1024)
    # Replace the last 64 bits of the multiple of 512 with the original message length
    # Divide into two chunks of 512 bits
    elif 448 <= L <= 512:
        bits.append(1)
        bits = pad_zero(bits, 1024, 'end')
        bits[-64:] = L_bit
        return chunker(bits, 512)

    # Otherwise, always put 1 at end
    # Loop until multiple of 512 + 64 bit of L_bit
    # Add the 64 bits representing the length of the message
    # Divide into two chunks of 512 bits
    else:
        bits.append(1)
        while (len(bits)+64) % 512 != 0:
            bits.append(0)
        bits = bits + L_bit
        return chunker(bits, 512)


def b2_to_b16(number):
    '''
    Function to covert from base=2 to base=16

    Parameters
    ----------
    number : list
        number in binary in a list (e.g. 2 = [1, 0])

    Returns
    -------
    h : string
        number in hexadecimal rappresentation
        (e.g. 15 = [1, 1, 1, 1] -> 'f')
    '''
    #convert to string
    value = ''.join([str(x) for x in number])
    #creat 4 bit chunks, and add bin-indicator
    binaries = []
    for d in range(0, len(value), 4):
        binaries.append('0b' + value[d:d+4])
    #transform to hexadecimal and remove hex-indicator
    h = ''
    for b in binaries:
        h += hex(int(b ,2))[2:]
    return h

#==========================================================================================
# Binary functions
#==========================================================================================

def If(i, y, z):
    return y if i == 1 else z


def And(i, j):
    return If(i, j, 0)


def AND(i, j):
    return [And(ii, jj) for ii, jj in zip(i, j)]


def Not(i):
    return If(i, 0, 1)


def NOT(i):
    return [Not(x) for x in i]


def xor(i, j):
    return If(i, Not(j), j)


def XOR(i, j):
    return [xor(ii, jj) for ii, jj in zip(i, j)]


def xorxor(i, j, l):
    return xor(i, xor(j, l))


def XORXOR(i, j, l):
    return [xorxor(ii, jj, ll) for ii, jj, ll, in zip(i, j, l)]


def maj(i,j,k):
    ''' Get the majority of results, i.e., if 2 or more of three values are the same
    '''
    return max([i,j,], key=[i,j,k].count)


def rotr(x, n):
    ''' rotate right
    Example
    -------
    >>> rotr(10011, 2)
    >>> 11100
    '''
    return x[-n:] + x[:-n]


def shr(x, n):
    ''' shift right
     Example
    -------
    >>> rotr(10011, 2)
    >>> 00100
    '''
    return n * [0] + x[:-n]


def add(i, j):
    '''
    Function to implement full binary adder
    (actually the carry over bit got neglected)
    '''
    L    = len(i)
    sums = list(range(L))
    # Initial input needs an carry over bit as 0
    c = 0
    for x in range(L-1,-1,-1):
        # Add the inout bits with a double xor gate
        sums[x] = xorxor(i[x], j[x], c)
        # Carry over bit is equal the most represented, e.g., output = 0,1,0
        # then 0 is the carry over bit
        c = maj(i[x], j[x], c)
    # Returns list of bits
    return sums

#==========================================================================================
# SHA function
#==========================================================================================

def sha_256(msg):
    '''
    Function to compute the fingerprint hash256

    Parameters
    ----------
    msg : string
        message to translate

    Returns
    -------
    result : string
        string in hexadecimal format with the encrypted message
    '''
    # Initializzetion of constants
    k = init(R)
    h0, h1, h2, h3, h4, h5, h6, h7 = init(init_h)
    # Pre process to prepare/divide the message
    chunks = pre_process(msg)

    for chunk in chunks:  # mail loop

        # Create lists of 32 bit words (512 bits / 32 = 16 words)
        w = chunker(chunk, 32)
        # Extend length of chunk to 64 words, the remaining 48
        for _ in range(48): # initialized with zeros
            w.append(32 * [0])

        for i in range(16, 64):
            s0   = XORXOR(rotr(w[i-15], 7), rotr(w[i-15], 18), shr(w[i-15], 3))
            s1   = XORXOR(rotr(w[i-2], 17), rotr(w[i-2] , 19), shr(w[i-2], 10))
            w[i] = add(add(add(w[i-16], s0), w[i-7]), s1)

        # Variables initializzation for the loop
        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        # And now some magic
        for j in range(64):
            S1    = XORXOR(rotr(e, 6), rotr(e, 11), rotr(e, 25) )
            ch    = XOR(AND(e, f), AND(NOT(e), g))
            temp1 = add(add(add(add(h, S1), ch), k[j]), w[j])
            S0    = XORXOR(rotr(a, 2), rotr(a, 13), rotr(a, 22))
            m     = XORXOR(AND(a, b), AND(a, c), AND(b, c))
            temp2 = add(S0, m)

            h = g; g = f; f = e
            e = add(d, temp1)
            d = c; c = b; b = a
            a = add(temp1, temp2)

        h0 = add(h0, a)
        h1 = add(h1, b)
        h2 = add(h2, c)
        h3 = add(h3, d)
        h4 = add(h4, e)
        h5 = add(h5, f)
        h6 = add(h6, g)
        h7 = add(h7, h)

    result = ''
    for val in [h0, h1, h2, h3, h4, h5, h6, h7]:
        result += b2_to_b16(val)

    return result
