import numpy as np

def cesar(msg, key, enc):
    """
    function for the Caesar cipher

    Parameters
    ----------
    msg : string
        message to encrypt or decrypt
    key : int
        encryption key
    enc : bool
        True for encrypt mesg, False to decrypt msg

    Return
    ------
    msg_c : string
        encrypted message or decrypted message
    """
    if not enc :
        key = - key #for decrypt

    msg_c = ""      #final message

    for l in msg:   #loop over original message

        if l.isalpha():                        #historically only the letters are encrypted

            val = ord(l)                       #from char to number
            val += key                         #encryption or decryption

            if l.isupper():                    #if l in msg is upper also in msg_c will be upper
                if val > ord('Z'): val -= 26   #periodical bounday condition
                if val < ord('A'): val += 26
            elif l.islower():                  #if l in msg is lower also in msg_c will be lower
                if val > ord('z'): val -= 26   #periodical bounday condition
                if val < ord('a'): val += 26

            msg_c += chr(val)    #output message must be a string

        else:
            msg_c += l           #the other characters are not encrypted

    return msg_c

if __name__ == "__main__":

    enc = int(input("Press 0 for decryption, 1 for encryption:\n"))

    text = input("\ninsert message:\n")

    print("\nThe key must be a number between 1 and 26, \n"
          "if you enter 27 it will be like having entered 1 and so on,\n"
          "the 0 key does not change the message\n")

    key = int(input("insert key:\n"))


    #text = 'Hi, how are you? Todo bien. Maremma canguro'
    #key = 13

    msg_enc = cesar(text, key, enc=enc)
    print("\nOutput message message:\n", msg_enc)


