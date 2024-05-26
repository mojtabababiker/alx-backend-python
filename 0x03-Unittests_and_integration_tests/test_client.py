#!/usr/bin/env python3
"""
Test module for the utils functions and methods
"""
from typing import Mapping, Tuple, Any
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient


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
        mocked_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org}")
