import unittest
from prog import *

import profile

class TestProg(unittest.TestCase):
    def test_prog(self):
        cant = 12
        result = sumaNaturales(cant)
        sol = 78
        self.assertEqual(result, sol)

if __name__ == '__main__':
    profile.run('print(sumaNaturales(12))')
    unittest.main()