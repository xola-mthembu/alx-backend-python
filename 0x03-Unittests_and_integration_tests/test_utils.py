#!/usr/bin/env python3
"""Test module for get_json function"""
import unittest
from unittest.mock import patch, Mock
from utils import get_json


class TestGetJson(unittest.TestCase):
    """Test case for get_json function"""

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """Test get_json returns correct payload"""
        mock_get.return_value = Mock(
            **{'json.return_value': {"payload": True}}
        )
        self.assertEqual(
            get_json("http://example.com"), {"payload": True}
        )
        mock_get.assert_called_once_with("http://example.com")

        # Reset mock for the next test case
        mock_get.reset_mock()

        mock_get.return_value = Mock(
            **{'json.return_value': {"payload": False}}
        )
        self.assertEqual(
            get_json("http://holberton.io"), {"payload": False}
        )
        mock_get.assert_called_once_with("http://holberton.io")


if __name__ == "__main__":
    unittest.main()
