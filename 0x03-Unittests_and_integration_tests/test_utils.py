#!/usr/bin/env python3
"""Test Module
"""
from parameterized import parameterized
import unittest
access_nested_map = __import__("utils")


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing the method access_nested_map
    """
    @parameterized([
        ({"a": 1}, ("a", )),
        ({"a": {"b": 2}}, ("a", "b")),
    ])
    def test_access_nested_map(self, nested_map, path):
        """Test the method to assert that it functions as req
        Args: None
        Returns: None
        """
        self.assertEqual(nested_map, path)
