from unittest import TestCase
from sum import summ as s
import pytest


class TestSumm(TestCase):
    def test_sum(self):

        print(s.sum(4,6))
        self.assertTrue(10,10)

    def test_sum_2(self):

        print(s.sum(4,6))
        self.assertEqual(10,11)