from typing import List
from pandas import DataFrame

import pandas as pd
import os


class CSVDataProcessor():

    def __init__(self, folderpath: str) -> None:
        if not os.path.isdir(folderpath):
            raise FileNotFoundError(f"❌ Invalid folder path: {folderpath}")
        self.folderpath: str = folderpath
        self.csv_files = self.list_files(".CSV")


    def load_csv(self) -> pd.DataFrame:
        self.refresh_files_list()
        if not self.csv_files:
           raise FileNotFoundError(f"❌ No CSV files found in {self.folderpath}")
        
        file_path = os.path.join(self.folderpath, self.csv_files[0])

        return pd.read_csv(file_path)


    def save_csv(self, df: pd.DataFrame, filename: str) -> None:
        self.refresh_files_list()
        full_path = f"{self.folderpath}/unioned_{filename}" 
        df.to_csv(full_path, index=False)


    def list_files(self, extension: str = None) -> List[str]:
        files = os.listdir(self.folderpath)
        return [f for f in files if f.lower().endswith(extension.lower())] if extension else files
    

    def refresh_files_list(self) -> None:
        self.csv_files = self.list_files(".CSV")



# if __name__ == '__main__':
#     csv = CSVDataProcessor("test_transactions")
#     df = csv.load_csv()
#     df.describe
    # print("YES")
    # print(df)
    
