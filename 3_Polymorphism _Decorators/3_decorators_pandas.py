def pandas_decorator(fx):
    def mainfunc(*args):
        response=fx(*args)
        # do some pandas processing
        response.to_parquet("/Users/sambitdan/Documents/PythonAdvancePractice/3_Polymorphism _Decorators/orders.parquet")
        return response

    return mainfunc

@pandas_decorator
def csv_to_parquet(file_path : str):
    import pandas as pd
    df=pd.read_csv(file_path)
    return df



response = csv_to_parquet(r'/Users/sambitdan/Documents/PythonAdvancePractice/1_OOP/files/orders.csv')
print(response)

