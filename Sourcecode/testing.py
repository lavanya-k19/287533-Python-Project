import unittest
from data import *

a = bloodgrp("jaiiii", "lavs", "gnanesh", "ram", "melav")
a.read_data(listt)


class TestDonor(unittest.TestCase):
    def test_search_donor(self):
        result = bloodgrp.search_donor(self, "8912345678")
        expected = "Finally Found"
        self.assertEqual(expected, result)

    def test_search_donor1(self):
        result = bloodgrp.search_donor(self, "8912345680")
        expected = "Sorry Not Found"
        self.assertEqual(expected, result)