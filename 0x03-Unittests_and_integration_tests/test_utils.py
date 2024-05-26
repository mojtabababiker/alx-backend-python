#!/usr/bin/env python3
"""
Test module for the utils functions and methods
"""
from typing import Mapping, Tuple, Any
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Main testing class for the utils.access_nested_map
    function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Tuple, expected: Any):
        """Test access nested map function for several senarios"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Tuple):
        """Test the KeyError raise for on the wrong Maps or paths"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Main testing class for the utils.get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Mapping):
        """Test the get_json function with multible inputs"""
        with patch("utils.requests.get") as mocked_get:
            # mocked_get.json.return_value = test_payload
            res = mocked_get.return_value
            res.json.return_value = test_payload
            result = get_json(test_url)
            mocked_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Main testing class for the utils.memoize decorator
    """
    def test_memoize(self):
        """Test the memoize decorator on a class method"""
        class TestClass:
            """A demo class for testing"""
            def a_method(self):
                """method a for testing"""
                return 42

            @memoize
            def a_property(self):
                """decorated function"""
                return self.a_method()

        with patch(f"{__name__}.TestMemoize.a_method",
                   create=True) as mocked_a:
            test_instance = TestClass()
            test_instance.a_method = mocked_a
            test_instance.a_property()
            test_instance.a_property()
            mocked_a.assert_called_once()
