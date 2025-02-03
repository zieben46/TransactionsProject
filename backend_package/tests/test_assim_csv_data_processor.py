import unittest
import os
import pandas as pd
import shutil
from tempfile import mkdtemp
from backend_package.main.csv_data_processor import CSVDataProcessor  # Assuming your class is in `csv_data_processor.py`

class TestCSVDataProcessorIntegration(unittest.TestCase):
    def setUp(self):
        """Create a temporary directory for testing"""
        self.test_folder = mkdtemp()  # Creates a temp folder
        self.processor = CSVDataProcessor(self.test_folder)

        # Create a test CSV file
        self.test_csv_filename = "test_file.CSV"
        self.test_csv_path = os.path.join(self.test_folder, self.test_csv_filename)
        self.test_df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})

        self.test_df.to_csv(self.test_csv_path, index=False)  # Write file

    def test_list_files(self):
        """Ensure `file_names()` correctly lists files in the folder"""
        expected_files = [self.test_csv_filename]
        self.assertEqual(sorted(self.processor.list_files()), sorted(expected_files))

    def test_load_csv(self):
        """Ensure `load_csv()` loads the first CSV file correctly"""
        df = self.processor.load_csv()
        pd.testing.assert_frame_equal(df, self.test_df)

    def test_save_csv(self):
        """Ensure `save_csv()` correctly writes a new CSV file"""
        new_filename = "output.CSV"
        self.processor.save_csv(self.test_df, new_filename)

        # Verify the file was written
        saved_path = os.path.join(self.test_folder, f"unioned_{new_filename}")
        self.assertTrue(os.path.exists(saved_path))

        # Verify the saved content
        saved_df = pd.read_csv(saved_path)
        pd.testing.assert_frame_equal(saved_df, self.test_df)

    def tearDown(self):
        """Remove the temporary test directory after tests"""
        shutil.rmtree(self.test_folder)

# if __name__ == "__main__":
#     unittest.main()
