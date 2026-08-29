import pandas as pd
class DataExt:

    def __init__(self, file_path : str):
        self.file_path = file_path

    def fetch_txt(self, separator : str):

        df = pd.read_csv(self.file_path, sep=separator)
        print(df.head())

    def fetch_json(self):
        
        df = pd.read_json(self.file_path)
        print(df.head())


    def fetch_parquet(self):
        
        df = pd.read_parquet(self.file_path)
        print(df.head())



obj = DataExt('/Users/sambitdan/Documents/PythonAdvancePractice/OOP/files/orders.csv')

obj.fetch_txt(',')

obj1 = DataExt('/Users/sambitdan/Documents/PythonAdvancePractice/OOP/files/orders.tsv')

obj1.fetch_txt('\t')

obj2 = DataExt('/Users/sambitdan/Documents/PythonAdvancePractice/OOP/files/orders.json')
obj2.fetch_json()

obj3 = DataExt('/Users/sambitdan/Documents/PythonAdvancePractice/OOP/files/orders.parquet')
obj3.fetch_parquet()
