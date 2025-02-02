from typing import List

import pandas as pd
import os


class CSVDataProcessor():

    def __init__(self, folderpath: str="transactions") -> None:
        self.folderpath: str = folderpath
        self.files_list: List[str] = self.file_names()

    def load_csv(self) -> pd.DataFrame:
       
        csv_files = [f for f in os.listdir(self.folderpath) if f.endswith(".CSV")]
        
        df = pd.read_csv(f"{self.folderpath}/{self.files_list[0]}")

        return df


    def save_csv(self, df: pd.DataFrame, filename: str) -> None:
        full_path = f"{self.folderpath}/unioned_{filename}"  # Ensure it saves as a .csv file
        df.to_csv(full_path, index=False)

    def file_names(self) -> List[str]:
        return os.listdir(self.folderpath)


if __name__ == '__main__':
    csv = CSVDataProcessor()
    df = csv.load_csv()
    print(df)
    pass
