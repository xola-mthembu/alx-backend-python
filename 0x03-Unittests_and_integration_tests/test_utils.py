#!/usr/bin/env python3
"""Test module for memoize decorator"""
import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test case for memoize decorator"""

    class TestClass:
        """Test class for memoize decorator"""

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_method):
        """Test memoize ensures a_method is called once"""
        test_obj = self.TestClass()
        self.assertEqual(test_obj.a_property, 42)
        self.assertEqual(test_obj.a_property, 42)
        mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
