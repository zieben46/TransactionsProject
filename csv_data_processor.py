class CSVDataProcessor():

    def __init__(self, filepath: str):
        self.filepath = filepath


def add_numbers(x: int, y: int) -> int:
    return x + y

result = add_numbers(10, "hello")  # ❌ This will fail due to type mismatch




if __name__ == '__main__':
    print("ran 3")
    processor = CSVDataProcessor(123)
    print("ran2")