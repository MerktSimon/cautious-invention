from unittest import TestCase

from cautious_invention import add


class TestAdd(TestCase):
    def test_identity(self):
        """This test makes sure that addition to zero does not fail"""
        a = 1
        actual = add(a,0)
        self.assertEqual(a, actual)

    def test_add_negation(self):
        a = 1
        actual = add(a, -a)
        self.assertEqual(0, actual)
