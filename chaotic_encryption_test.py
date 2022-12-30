"""
test for chaotic encryption with photo
"""
import time
from PIL import Image

import chaotic_map
import chaotic_encryption

start = time.time()

def test(k, img, key_func, args=()):
    """
    test function

    Parameter
    ---------
    k : int
        number for grafic
    img : Pil object
        photo to encrypt
    key_func : callable
        function for generating keys
    args : tuple
        extra argument to pass to key_func

    Return
    ------
    img_e : ndarray
        matrix of encrypted photo
    img_d : ndarray
        matrix of decrypted photo
    """

    msg_m = np.array(img)

    row, col, dim = msg_m.shape
    N = row * col * dim

    #generation key
    key = key_func(*args, N)

    #we want array
    msg = np.reshape(msg_m, N)

    msg_e = chaotic_encryption.encrypt(msg,   key, N, enc=True)   #encrypt
    msg_d = chaotic_encryption.encrypt(msg_e, key, N, enc=False)  #decrypt

    img_e = np.reshape(msg_e, (row, col, dim)) #back to matrix
    img_d = np.reshape(msg_d, (row, col, dim)) #back to matrix

    chaotic_encryption.plot_photo_hist(msg_m, img_e, row, col, k)

    return img_e, img_d


#read image
img = Image.open(r"C:\Users\franc\Documents\codici python\crittografia\prova_foto\furios.jpeg")


##Test with logistic
#Parameter key generation
r  = 3.99 #be sure you are in chaos (funny to see encrypted message not in chaos)
x0 = 0.5

img_e, img_d = test(1, img, chaotic_map.logistic_key, args=(x0, r))

#save images
img_2 = Image.fromarray(np.uint8(img_e))
img_2 = img_2.save(r"C:\Users\franc\Documents\codici python\crittografia\prova_foto\log_furios_enc.png")
img_3 = Image.fromarray(np.uint8(img_d))
img_3 = img_3.save(r"C:\Users\franc\Documents\codici python\crittografia\prova_foto\log_furios_dec.png")


##Test with tent
#Parameter key generation
mu = 1.99 #be sure you are in chaos
x0 = 0.5

img_e, img_d = test(2, img, chaotic_map.tent_key, args=(x0, mu))

#save images
img_2 = Image.fromarray(np.uint8(img_e))
img_2 = img_2.save(r"C:\Users\franc\Documents\codici python\crittografia\prova_foto\tent_furios_enc.png")
img_3 = Image.fromarray(np.uint8(img_d))
img_3 = img_3.save(r"C:\Users\franc\Documents\codici python\crittografia\prova_foto\tent_furios_dec.png")


##Test with gaussian
#Parameter key generation
a = 10  #be sure you are in chaos
b = -0.6
x0 = 0.2

img_e, img_d = test(3, img, chaotic_map.gaussian_key, args=(x0, a, b))

#save images
img_2 = Image.fromarray(np.uint8(img_e))
img_2 = img_2.save(r"C:\Users\franc\Documents\codici python\crittografia\prova_foto\gauss_furios_enc.png")
img_3 = Image.fromarray(np.uint8(img_d))
img_3 = img_3.save(r"C:\Users\franc\Documents\codici python\crittografia\prova_foto\gauss_furios_dec.png")


##Test with generalized logistic
#Parameter key generation
p  = 0.2 #be sure you are in chaos
q  = 1
x0 = 0.1

img_e, img_d = test(4, img, chaotic_map.generalized_logistic_key, args=(x0, p, q))

#save images
img_2 = Image.fromarray(np.uint8(img_e))
img_2 = img_2.save(r"C:\Users\franc\Documents\codici python\crittografia\prova_foto\glog_furios_enc.png")
img_3 = Image.fromarray(np.uint8(img_d))
img_3 = img_3.save(r"C:\Users\franc\Documents\codici python\crittografia\prova_foto\glog_furios_dec.png")



end = time.time() - start
print(f'Elapsed time = {end:.3f} seconds')