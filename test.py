import unittest
from prime_numbers import is_prime_number, get_prime_numbers


class IsPrimeNumberTest(unittest.TestCase):
    def test_one_is_not_prime(self):
        self.assertFalse(is_prime_number(1))

    def test_four_is_not_prime(self):
        self.assertFalse(is_prime_number(4))

    def test_seven_is_prime(self):
        self.assertTrue(is_prime_number(7))

    def test_five_is_prime(self):
        self.assertTrue(is_prime_number(5))

class GetPrimeNumbers(unittest.TestCase):
    def test_limit_100(self):
        self.assertEqual(len(get_prime_numbers(1, 100)), 100)

    def test_limit_234(self):
        self.assertEqual(len(get_prime_numbers(1, 234)), 234)

    def test_limit_10000(self):
        self.assertEqual(len(get_prime_numbers(10000,10000)),10000)

    def test_1_to_4_are_prime(self):
        for number in get_prime_numbers(1,4):
            self.assertTrue(is_prime_number(number))

    def test_5_to_9_are_prime(self):
        for number in get_prime_numbers(5,9):
            self.assertTrue(is_prime_number(number))

    def test_1000000_to_1004_are_prime(self):
        for number in get_prime_numbers(1000000,1004):
            self.assertTrue(is_prime_number(number))

#get_prime_numbers(100000,10000))
if __name__ == '__main__':
    unittest.main()
