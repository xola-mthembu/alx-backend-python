#!/usr/bin/env python3
"""Test module for access_nested_map exceptions"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function"""

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, err_msg):
        """Test that KeyError is raised with correct message"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{err_msg}'")


if __name__ == "__main__":
    unittest.main()
