import unittest
import pandas as pd
from unittest.mock import patch
from io import StringIO
from data import *

class EXAMINECSVTest(unittest.TestCase):

    def setUp(self):
        # Create an instance of your class
        self.test_instance = EXAMINECSV()

    @patch('sys.stdout', new_callable=StringIO)
    def test_get_distinct_years(self, mock_stdout):
        expected_result = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]  # Adjust based on your data

        # Call the method
        self.test_instance.get_distinct_years()

        # Get the printed output
        printed_output = mock_stdout.getvalue().strip()

        # Convert the printed output to a list of integers
        result = [int(year) for year in printed_output.split()]

        # Assert that the result matches the expected result
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


