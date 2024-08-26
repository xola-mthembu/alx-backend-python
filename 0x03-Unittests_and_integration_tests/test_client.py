#!/usr/bin/env python3
"""Unit and integration tests for GithubOrgClient."""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that org returns the correct result."""
        client_instance = GithubOrgClient(org_name)
        client_instance.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url is correct."""
        mock_org.return_value = {
            'repos_url': (
                "https://api.github.com/orgs/sample_org/repos"
            )
        }
        client_instance = GithubOrgClient("sample_org")
        self.assertEqual(
            client_instance._public_repos_url,
            "https://api.github.com/orgs/sample_org/repos"
        )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns correct repo list."""
        sample_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = sample_payload

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = (
                "https://api.github.com/orgs/sample/repos"
            )
            client_instance = GithubOrgClient("sample")
            result = client_instance.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license works correctly."""
        client_instance = GithubOrgClient("sample")
        self.assertEqual(client_instance.has_license(repo,
                         license_key), expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up mock before any test methods."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return Mock(**{'json.return_value': cls.org_payload})
            return Mock(**{'json.return_value': cls.repos_payload})

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop mock after all test methods."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns correct repos."""
        client_instance = GithubOrgClient("google")
        self.assertEqual(client_instance.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license filter."""
        client_instance = GithubOrgClient("google")
        self.assertEqual(
            client_instance.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == '__main__':
    unittest.main()
