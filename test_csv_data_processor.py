import unittest
from csv_data_processor import CSVDataProcessor


class TestCSVDataProcessor(unittest.TestCase):

    def test_has_filepath_attr(self) -> None:

        instance = CSVDataProcessor(filepath = "")

        instance2 = "ssdfsdfsdf"

        self.assertTrue(hasattr(instance, "filepath"))

    # def test_invalid_filepath_results_in_fails(self) -> None:
    #     pass

        # invalid_filepath: int = 1
        # CSVDataProcessor(2)


 #       with self.assertRaises(TypeError):
 #           CSVDataProcessor(filepath = 1)



    # def test_has_csvs_returns_true_if_folder_has_at_least_one_csv(self):
    #     mock


if __name__ == '__main__':
    CSVDataProcessor(filepath = "")
    print("why no error")
    # unittest.main()  # pragma: no cover





# def add_numbers(x: int, y: int) -> int:
#     return x + 



# def add_numbers2(x, y) -> int:
#     return x + y
