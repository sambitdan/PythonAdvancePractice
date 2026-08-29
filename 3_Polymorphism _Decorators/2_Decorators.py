# Decorator is use to enhance our existing functions
#  We can enhance our functions by using decorators on top of that decorators are also a kind of functions
# Rember decorators are used only on top of a function

def my_decorator(func):  # this function is defining the decorator through which we will pass the function
    def main_function(*args): # main function will run the function or decorate the funcion and we are calling all the params through *args
        print("Before Calling the function")
        response = func(*args)  # Here we are calling the decorated function and passing the arguments
        return response
        print("after calling the function")

        
    return main_function


@my_decorator
def fetch_data(url : str , path : str):
    return f"Fetching data from {url} and saving to {path}"


print(fetch_data("https://api.example.com/data","/tmp/data.json"))

