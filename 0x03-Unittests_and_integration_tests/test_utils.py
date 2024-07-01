#!/usr/bin/env python3
"""Test Module
"""
from parameterized import parameterized
import unittest
access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing the method access_nested_map
    """
    @parameterized([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expect):
        """Test the method to assert that it functions as req
        Args: None
        Returns: None
        """
        self.assertEqual(access_nested_map(nested_map, path), expect)
