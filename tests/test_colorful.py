import unittest
from colorful import is_colorful

class ColorfulTest(unittest.TestCase):
    def test_with_duplicate_numbers(self):
        self.assertEqual(is_colorful(23425), False)
        self.assertEqual(is_colorful(43425), False)

    def test_with_zero_or_one(self):
        self.assertEqual(is_colorful(1234), False)
        self.assertEqual(is_colorful(3204), False)

    def test_single_number(self):
        for k in range(10):
            self.assertTrue(is_colorful(k))

    def test_colorful_number(self):
        self.assertTrue(is_colorful(3245))
