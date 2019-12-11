# -*- coding: utf-8 -*-
"""This file contains the tests of cautious invention."""

from unittest import TestCase

from cautious_invention import add


class TestAdd(TestCase):
    """This is a test class."""

    def test_identity(self):
        """This test makes sure that addition to zero does not fail."""
        a = 1
        actual = add(a, 0)
        self.assertEqual(a, actual)

    def test_add_negation(self):
        """Test add negation."""
        a = 1
        actual = add(a, -a)
        self.assertEqual(0, actual)
