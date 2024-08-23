#!/usr/bin/env python3
"""Test module for GithubOrgClient._public_repos_url"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient._public_repos_url"""

    @patch('client.GithubOrgClient.org', new_callable=patch.PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url returns expected URL"""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test/repos"
        }
        client = GithubOrgClient("test")
        self.assertEqual(
            client._public_repos_url,
            "https://api.github.com/orgs/test/repos"
        )


if __name__ == "__main__":
    unittest.main()
