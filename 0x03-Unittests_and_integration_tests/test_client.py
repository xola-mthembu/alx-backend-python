#!/usr/bin/env python3
"""Integration test for GithubOrgClient"""
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test case for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up class for integration tests"""
        patcher = patch('requests.get')
        cls.get_patcher = patcher.start()
        cls.get_patcher.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class after tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method returns expected repo names"""
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license filtering"""
        client = GithubOrgClient("test")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
