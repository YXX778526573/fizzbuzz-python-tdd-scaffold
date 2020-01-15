import unittest
from Fizz import FizzBuzz

class test(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual("FizzBuzz",FizzBuzz(30))
        self.assertEqual("Fizz",FizzBuzz(3))
        self.assertEqual("Buzz",FizzBuzz(10))
        self.assertEqual(31,FizzBuzz(31))

if __name__ == '__main__':
    unittest.main()
