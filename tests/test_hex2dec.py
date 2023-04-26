import unittest
from git_practice import hex2dec

class TestHex2dec(unittest.TestCase):
    def test_should_return_with_valid_chars(self):
        self.assertEqual(hex2dec.hex_to_decimal("0"), 0)
        self.assertEqual(hex2dec.hex_to_decimal("A"), 10)
        self.assertEqual(hex2dec.hex_to_decimal("B"), 11)
        self.assertEqual(hex2dec.hex_to_decimal("C"), 12)
        self.assertEqual(hex2dec.hex_to_decimal("D"), 13)
        self.assertEqual(hex2dec.hex_to_decimal("E"), 14)
        self.assertEqual(hex2dec.hex_to_decimal("F"), 15)

    def test_should_raise_with_invalid_string(self):
        with self.assertRaises(ValueError):
            hex2dec.hex_to_decimal("hello")

if __name__ == "__main__":
    unittest.main()
