import unittest
from unittest.mock import mock_open, patch, MagicMock
import pandas as pd
import os
from io import StringIO


from csv_data_processor import CSVDataProcessor



"""
read csvs, give them schema, union into one

"""



class TestCSVDataProcessor(unittest.TestCase):

    def setUp(self):
        """Setup method that runs before each test"""
        self.instance = CSVDataProcessor()
        self.test_df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
        self.test_folder = "transactions"

    def test_has_filepath_attr(self) -> None:
        self.assertTrue(hasattr(self.instance, "folderpath"))

    @patch("pandas.read_csv")
    def test_load_csv_mock(self, mock_read_csv):

        # Mock the return value of `pd.read_csv`
        mock_read_csv.return_value =  self.test_df
        # Create an instance of CSVDataProcessor (real filepath is irrelevant)

        # Mocked `pd.read_csv()` will return fake data
        df = self.instance.load_csv()

        expected_data = {"col1": [1, 2], "col2": ["a", "b"]}
        pd.testing.assert_frame_equal(df, pd.DataFrame(expected_data))

        mock_read_csv.assert_called()

    @patch("pandas.DataFrame.to_csv")  # Mock pandas' to_csv method
    def test_save_csv_mock(self, mock_to_csv):
        # Create a sample DataFrame
        df = self.test_df

        # Create an instance of CSVDataProcessor
        
        # Call save_csv (this should trigger the mock)
        self.instance.save_csv(df, "mock_output.csv")

        # Ensure `to_csv()` was called once with the expected arguments
        mock_to_csv.assert_called_once_with("transactions/unioned_mock_output.csv", index=False)


    @patch("os.listdir")
    def test_file_names_in_folder_mock(self, mock_listdir):
        """Mock os.listdir() to check if expected files are present"""
        # Mock the return value of os.listdir
        mock_listdir.return_value = ["file1_unioned.csv", "file2_unioned.csv", "other_file.txt"]

        # Call the method under test
        files = self.instance.file_names()

        # Expected files
        expected_files = ["file1_unioned.csv", "file2_unioned.csv"]

        # Verify expected files are in the folder
        for file in expected_files:
            self.assertIn(file, files)

        # Ensure os.listdir was called with the correct folder
        mock_listdir.assert_called_once_with(self.test_folder)



if __name__ == '__main__':
    unittest.main()  # pragma: no cover

