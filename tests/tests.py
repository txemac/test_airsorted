import unittest
import os
from src.airsorted import AirSorted

__author__ = 'josebermudez'


class TestAirsorted(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestAirsorted, self).__init__(*args, **kwargs)

        self.airsorted = AirSorted()

        self.path = os.path.realpath('')

        self.bookings = [
            {
                "start": "2015-06-01",
                "end": "2015-06-15"
            },
            {
                "start": "2015-06-19",
                "end": "2015-06-27"
            }
        ]

        self.year = [
            {
                "start": "2015-06-01",
                "end": "2015-06-15"
            },
            {
                "start": "2015-06-13",
                "end": "2015-06-27"
            },
            {
                "start": "2015-02-01",
                "end": "2015-02-15"
            },
            {
                "start": "2015-02-18",
                "end": "2015-02-27"
            },
            {
                "start": "2015-12-01",
                "end": "2015-12-15"
            },
            {
                "start": "2015-12-18",
                "end": "2015-12-27"
            }
        ]

    def test_bookings(self):
        expected_out = "Available:\n2015-06-16\n2015-06-17\n2015-06-18\n2015-06-28\n2015-06-29\n2015-06-30\n"
        out = self.airsorted.to_print(self.bookings)
        self.assertEqual(out, expected_out)

    def test_file_month(self):
        filename = os.path.join(self.path, 'out_month.html')

        if os.path.isfile(filename):
            os.remove(filename)

        self.airsorted.to_file_month(self.bookings, filename=filename)

        # check new file
        self.assertTrue(os.path.isfile(filename))

    def test_file_year(self):
        filename = os.path.join(self.path, 'out_year.html')

        if os.path.isfile(filename):
            os.remove(filename)

        self.airsorted.to_file_year(self.year, filename=filename)

        # check new file
        self.assertTrue(os.path.isfile(filename))
