#!/usr/bin/env python3
"""
Module for integration tests for client.py.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """
    Integration test case for GithubOrgClient.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test GithubOrgClient.org method with parameterized input.
        """
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test _public_repos_url property.
        """
        mock_org.return_value = {"repos_url": "http://repos_url.com"}
        client = GithubOrgClient("org_name")
        self.assertEqual(
            client._public_repos_url,
            "http://repos_url.com"
        )

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test public_repos method to ensure correct behavior.
        """
        # Mock _public_repos_url to return a specific URL
        mock_public_repos_url.return_value = "http://repos_url.com"

        # Mock get_json to return a fake payload
        mock_get_json.return_value = [
            {"name": "repo1"}, {"name": "repo2"}
        ]

        client = GithubOrgClient("org_name")
        self.assertEqual(
            client.public_repos(),
            ["repo1", "repo2"]
        )

        # Ensure the _public_repos_url property was called once
        mock_public_repos_url.assert_called_once()

        # Ensure the get_json function was called once with the mocked URL
        mock_get_json.assert_called_once_with("http://repos_url.com")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test has_license method.
        """
        client = GithubOrgClient("org_name")
        self.assertEqual(
            client.has_license(repo, license_key),
            expected
        )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
        (org_payload, repos_payload, expected_repos, apache2_repos)
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test case for GithubOrgClient using fixtures.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class by patching requests.get.
        """
        cls.get_patcher = patch(
            'requests.get',
            side_effect=cls.get_patcher_fn
        )
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def get_patcher_fn(cls, url):
        """
        Side effect function for patching requests.get.
        """
        if url == 'https://api.github.com/orgs/google':
            return cls.org_payload
        elif url == 'https://api.github.com/orgs/google/repos':
            return cls.repos_payload
        return None

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test class by stopping the patcher.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method using fixture data.
        """
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(),
            self.expected_repos
        )

    def test_public_repos_with_license(self):
        """
        Test public_repos method filtering by license using fixture data.
        """
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
