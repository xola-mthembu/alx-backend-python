#!/usr/bin/env python3
"""Test module for GithubOrgClient.has_license"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient.has_license"""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns correct boolean"""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected
        )


if __name__ == "__main__":
    unittest.main()
