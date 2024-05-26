#!/usr/bin/env python3
"""
Test module for the utils functions and methods
"""
from typing import Mapping, Tuple, Dict, Any
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


org_payload, repos_payload, expected_repos, apache2_repos = TEST_PAYLOAD[0]


class TestGithubOrgClient(unittest.TestCase):
    """
    Main testing class for the client.GithubOrgClient
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json", return_value={})
    def test_org(self, org: str, mocked_get_json: Mock):
        """Test the client.GithubOrgClient.org method"""
        client = GithubOrgClient(org)
        self.assertDictEqual(client.org, {})
        mocked_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self):
        """Test the public_repos_url method"""
        payload = {"org": "Alx-sw",
                   "repos_url": ".../repos_url"
                   }
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mocked_org:
            mocked_org.return_value = payload
            client = GithubOrgClient("alx-sw")
            result = client._public_repos_url
            self.assertEqual(result, payload['repos_url'])

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json):
        """Test GithubOrgClient.public_repos mthod"""
        repos = [
                {"name": "repo1"},
                {"name": "repo2"},
                {"name": "repo3"},
                {"name": "repo4"}
        ]

        mocked_get_json.return_value = repos

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mocked_pru:
            mocked_pru.return_value = ".../repos_url"
            client = GithubOrgClient("alx-sw")
            self.assertListEqual(
                client.public_repos(), [repo["name"] for repo in repos]
            )
            mocked_pru.assert_called_once()
            mocked_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expc: bool):
        """Test ithubOrgClient.has_license method"""
        client = GithubOrgClient("alx-sw")
        result = client.has_license(repo, license_key)
        self.assertTrue(result is expc)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'),
                     [(org_payload, repos_payload,
                       expected_repos, apache2_repos)])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """An intergration test for the GithubOrgClient class"""
    @classmethod
    def setupClass(cls):
        """setup the patcher and the other environment for test"""
        def side_effect(url: str) -> Dict:
            """Returns he correct fixtures for the various values of url
            that you anticipate to receive"""
            res = Mock()
            if url.endswith('repos'):
                res.json.return_value = repos_payload
                return res
            res.json.return_value = org_payload
            return res

        get_patcher = patch("requests.get", side_effect=side_effect)
        TestIntegrationGithubOrgClient.get_patcher = get_patcher
        TestIntegrationGithubOrgClient.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """clear the patcher and remove the test envirionment"""
        TestIntegrationGithubOrgClient.get_patcher.stop()
