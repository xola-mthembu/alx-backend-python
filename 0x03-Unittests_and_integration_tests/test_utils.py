#!/usr/bin/env python3
"""
Module for unit tests for utils.py.
"""

import unittest
from parameterized import parameterized
from utils import (
    access_nested_map, get_json, memoize
)  # Shortened import line to meet 79 characters limit
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for access_nested_map function in utils module.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function with parameterized inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """
        Test access_nested_map function to raise KeyError.
        """
        with self.assertRaises(KeyError) as ctx:
            access_nested_map(nested_map, path)
        self.assertEqual(str(ctx.exception), f"'{exception}'")


class TestGetJson(unittest.TestCase):
    """
    Test case for get_json function in utils module.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function to ensure it returns the expected payload.
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(
            get_json(test_url),
            test_payload
        )
        mock_get.assert_called_once_with(
            test_url
        )


class TestMemoize(unittest.TestCase):
    """
    Test case for memoize decorator in utils module.
    """

    def test_memoize(self):
        """
        Test memoize decorator functionality.
        """

        class TestClass:
            """
            Test class to demonstrate memoize decorator.
            """

            def a_method(self):
                """
                Returns 42.
                """
                return 42

            @memoize
            def a_property(self):
                """
                Memoized method that returns the result of a_method.
                """
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_method:
            instance = TestClass()
            self.assertEqual(
                instance.a_property, 42
            )  # First call, should call a_method
            self.assertEqual(
                instance.a_property, 42
            )  # Second call, should use memoized result
            mock_method.assert_called_once()
