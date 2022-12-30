"""
code for encrypting and decrypting
a message using the logistic map
"""
import numpy as np
import matplotlib.pyplot as plt


def encrypt(msg, key, size, enc):
    """
    function that encrypts the message
    despite the name, in reality this
    function can also decrypt the message,
    just rewind the procedure,
    i.e. send the inputs reversed.
    This is because xor is the inverse of itself

    Parameter
    ---------
    msg : 1darray
        message to encrypt
    key : 1darray
        message to decrypt
    size : int
        size of message
    enc : bool
        True for encrypt, False for decrypt

    Return
    ------
    out : 1darray
        encrypted or decrypted message
    """
    #for decrypt
    if not enc :
        key = key[::-1]
        msg = msg[::-1]
    else :
        pass

    key = key*255                        #so it is compatible with RGB
    key = key.astype('int64')            #we want integers

    out = np.zeros(size, dtype='int64')  #output

    for i in range(size):                #loop over message

        out[i] = msg[i]^key[i]           #a ^ b = XOR(a, b)
                                         #we don't need (no education)
                                         #to switch to binary

    #for decrypt
    if not enc :
        out = out[::-1]
    else :
        pass

    return out


def plot_photo_hist(msg_1, msg_2, row, col, k):
    """
    make plot of histogram of colors
    for encrypted and non ecrypted photo

    Parameters
    ----------
    msg_1 : 3darray
        original photo
    msg_2 : 3darray
        encrypted photo
    raw, col : int
        dimension of matrix for the several layer (RGB)
    """

    plt.figure(k)
    plt.suptitle("Istogramma valori RGB")
    y_l = ["R", "G", "B"]
    for i in range(3):
        y1 = np.reshape(msg_1[:, :, i], row*col)
        y2 = np.reshape(msg_2[:, :, i], row*col)

        plt.subplot(3, 2, 2*i+1)
        plt.title("Prima della crittografia")
        plt.hist(y1, bins=int(np.sqrt(row*col)-0.582*np.sqrt(row*col)), density=True)
        plt.ylabel(y_l[i])
        plt.grid()

        plt.subplot(3, 2, 2*i+2)
        plt.title("Dopo la crittografia")
        plt.hist(y2, bins=int(np.sqrt(row*col)-0.582*np.sqrt(row*col)), density=True)
        plt.grid()

    plt.show()

