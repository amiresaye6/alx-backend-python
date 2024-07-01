#!/usr/bin/env python3
"""
0. Parameterize a unit test
"""
import unittest
from utils import access_nested_map
from typing import Mapping, Any, Sequence
from parameterized import parameterized


class TestAccessNestedMap (unittest.TestCase):
    """
    test class for the access_nested_map method
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        Test method to verify that the method returns the expected result.

        Args:
            nested_map (Mapping): A nested mapping object.
            path (Sequence): A sequence representing the path to access a value
            in the nested map.
            expected (int): The expected value to be returned by the method.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
