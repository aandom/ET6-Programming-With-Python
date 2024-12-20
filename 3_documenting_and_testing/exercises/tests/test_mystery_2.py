import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """Test the mystery_2 function"""

    # def test_minimal_list_input(self):
    #     """"""
    #     self.assertEqual(mystery_2([]), None)

    # def test_minimal_string_input(self):
    #     """"""
    #     self.assertEqual(mystery_2(''), None)

    def test_empty_list_returns_none(self):
        """Test that an empty list returns None."""
        self.assertEqual(mystery_2([]), None)

    def test_empty_string_returns_none(self):
        """Test that an empty string returns None."""
        self.assertEqual(mystery_2(''), None)

    def test_non_empty_list_returns_length(self):
        """Test that a non-empty list returns its length."""
        self.assertEqual(mystery_2([1, 2, 3]), 3)

    def test_non_empty_string_returns_length(self):
        """Test that a non-empty string returns its length."""
        self.assertEqual(mystery_2("hello"), 5)

    def test_tuple_returns_length(self):
        """Test that a tuple returns its length."""
        self.assertEqual(mystery_2((1, 2)), 2)

    def test_non_iterable_raises_type_error(self):
        """Test that a non-iterable input raises a TypeError."""
        with self.assertRaises(TypeError):
            mystery_2(10)
