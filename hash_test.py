import math
import hashlib
import unittest

from hash import sha_256
from hash_constant import *


msg = "ok this is a test, mabey all will be good"


class TESTS(unittest.TestCase):

    def test_sha256(self):
        ''' Litte test
        '''
        result     = sha_256(msg)
        result_lib = hashlib.sha256(msg.encode('utf-8')).hexdigest()

        print("res:", result)
        print("lib:", result_lib)

        self.assertEqual(result, result_lib)

        B = 2**32
        x = 2**(1/2)
        y = 2**(1/3)

        x_dec = math.modf(x)[0]
        y_dec = math.modf(y)[0]

        # Converison
        init_h_0 = hex(int(x_dec * B))
        R_0      = hex(int(y_dec * B))

        print(init_h_0, init_h[0])
        print(R_0, R[0])

        self.assertEqual(init_h_0, init_h[0])
        self.assertEqual(R_0, R[0])


if __name__ == '__main__':
    unittest.main()
