"""
Vigenère cipher
"""


def vigenere(msg, key, enc):
    """
    function for the Vigenère cipher

    Parameters
    ----------
    msg : string
        message to encrypt or decrypt
    key : int
        encryption key
    enc : bool
        True for encrypt msg, False to decrypt msg

    Return
    ------
    msg_c : string
        encrypted message or decrypted message
    """
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'                    #alfabeto
    al_to_nu = dict(zip(alfabeto, range(0, 25)))               #from letter to number
    nu_to_al = dict(zip(al_to_nu.values(), al_to_nu.keys()))   #from number to letter

    msg_c = ""                        #final message

    for i, l in enumerate(msg):       #loop over original message

        up = 0                        #to remember if l is upper
        if l.isalpha():               #historically only the letters are encrypted

            if l.isupper() :          #if l is upper we change in lower
                up = 1                #but at fisnish run we remember and
                l = l.lower()         #change again

            val_m = al_to_nu[l]
            val_k = al_to_nu[key[i % len(key)]]

            if not enc :
                val_k *= -1           #to decrypt

            val_e = (val_m + val_k)%26
            new_c = nu_to_al[val_e]

            if up != 0:               #if l was upper so also the
                new_c = new_c.upper() #encrypted char will be upper

            msg_c += new_c
            up = 0                    #reset to zero

        else:
            msg_c += l                #the other characters are not encrypted

    return msg_c


if __name__ == "__main__":

    enc = int(input("Press 0 for decryption, 1 for encryption:\n"))

    text = input("\ninsert message:\n")

    key = input("\ninsert key:\n").lower()

    msg_enc = vigenere(text, key, enc=enc)
    print("\nOutput message message:\n", msg_enc)