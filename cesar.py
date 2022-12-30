import numpy as np

def cesar(msg, key, enc):
    """
    function for the Caesar cipher

    Parameters
    ----------
    msg : string or 1darray
        message to encrypt or decrypt
    key : int
        encryption key
    enc : bool
        True for encrypt mesg, False to decrypt msg

    Return
    ------
    msg_e : 1d array
        encrypted message
    or
    msg_d_text : string
        decrypted message
    """
    if enc :
        N = len(msg)

        #from char to number
        msg_e  = np.zeros(N, dtype='int64')
        for i, l in enumerate(msg):
            msg_e[i] = ord(l)

        msg_e += key

        return msg_e

    else :
        msg_d = msg - key

        #from number to char
        msg_d_text = ""
        for l in msg_d:
            msg_d_text += chr(l)

        return msg_d_text


text = 'Hi, how are you? Todo bien. Maremma canguro'
key = 15

msg_enc = cesar(text, key, enc=True)
print("crypted message:\n", msg_enc)

msg_dec = cesar(msg_enc, key, enc=False)
print("encrypted message:\n", msg_dec)

