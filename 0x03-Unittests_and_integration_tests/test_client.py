#!/usr/bin/env python3
"""Test module for GithubOrgClient.public_repos"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient.public_repos"""

    @patch('client.get_json', return_value=[
        {"name": "repo1", "license": {"key": "mit"}},
        {"name": "repo2", "license": {"key": "apache-2.0"}},
    ])
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=patch.PropertyMock)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """Test public_repos returns expected repo names"""
        mock_repos_url.return_value = "https://api.github.com/orgs/test/repos"
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
