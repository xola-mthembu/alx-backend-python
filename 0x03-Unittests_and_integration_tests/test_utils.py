#!/usr/bin/env python3
"""Unit test for utils.access_nested_map"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """Test that access_nested_map raises expected exception"""
        with self.assertRaises(exception) as context:
            access_nested_map(nested_map, path)
        if isinstance(nested_map, dict) and len(path) > 1:
            self.assertEqual(
                str(context.exception),
                f"KeyError: '{path[-1]}'"
            )


if __name__ == '__main__':
    unittest.main()
