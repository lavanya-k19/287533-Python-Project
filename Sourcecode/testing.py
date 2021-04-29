import unittest
from donor import *

a = blooddb("jaiiii", "lavs", "gnanesh", "ram", "melav")
a.read_data(listt)


class TestDonor(unittest.TestCase):
    def test_search_donor(self):
        result = blooddb.search_donor(self, "8912345678")
        expected = "Found"
        self.assertEqual(expected, result)

    def test_search_donor1(self):
        result = blooddb.search_donor(self, "8912345680")
        expected = "Not Found"
        self.assertEqual(expected, result)