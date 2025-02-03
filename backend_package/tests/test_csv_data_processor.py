import unittest
from unittest.mock import mock_open, patch, MagicMock
import pandas as pd
import os
from io import StringIO

from backend_package.main.csv_data_processor import CSVDataProcessor



class TestCSVDataProcessor(unittest.TestCase):
    
    TEST_FOLDERPATH = "test_transactions"

    def test_invalid_instance_bad_folderpath(self):
        with self.assertRaises(FileNotFoundError) as context:
            CSVDataProcessor("bad_folderpath")  # Should raise an error


    def test_has_attributes(self) -> None:
        self.processor = CSVDataProcessor(self.TEST_FOLDERPATH)
        self.assertTrue(hasattr(self.processor, "folderpath"))
        self.assertTrue(hasattr(self.processor, "csv_files"))


    def setUp(self):
        """Setup method that runs before each test"""
        self.processor = CSVDataProcessor(self.TEST_FOLDERPATH)
        self.test_df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
         

    @patch("pandas.read_csv")
    def test_load_csv_mock(self, mock_read_csv: MagicMock):
        mock_read_csv.return_value =  self.test_df
        df = self.processor.load_csv()
        expected_data = {"col1": [1, 2], "col2": ["a", "b"]}
        pd.testing.assert_frame_equal(df, pd.DataFrame(expected_data))
        mock_read_csv.assert_called()


    @patch("pandas.DataFrame.to_csv")  # Mock pandas' to_csv method
    def test_save_csv_mock(self, mock_to_csv: MagicMock):
        df = self.test_df
        self.processor.save_csv(df, "mock_output.csv")
        mock_to_csv.assert_called_once_with("test_transactions/unioned_mock_output.csv", index=False)


    @patch("os.listdir")
    def test_list_files_in_folder_mock(self, mock_listdir: MagicMock):
        mock_listdir.return_value = ["file1_unioned.csv", "file2_unioned.csv", "other_file.txt"]
        files = self.processor.list_files()
        expected_files = ["file1_unioned.csv", "file2_unioned.csv"]
        [self.assertIn(file, files) for file in expected_files]
        mock_listdir.assert_called_once_with(self.processor.folderpath)




# if __name__ == '__main__':
#     unittest.main()  # pragma: no cover

