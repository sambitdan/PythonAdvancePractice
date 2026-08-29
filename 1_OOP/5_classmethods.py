class MyClass:
    var1 = '100'
    var2 = '500'

    # Dunder methods or magic methods are special methods in Python that have double underscores at the beginning and end of their names.
    #  They are used to define the behavior of objects in Python and are called automatically by the interpreter in certain situations.

    def __init__(self):
        print("This is the constructor method. It is called when we create an instance of the class.")

    def __str__(self):
        return f"This is the string representation of the object. var1: {self.var1}, var2: {self.var2}"

    # Changing the value of class variable using instance method (our default method is instance method)
    def change_var1(self, new_value):
        MyClass.var1 = new_value


    #cls is a reference to the class itself,
    # not an instance of the class. It allows us to access and modify class variables. 
    # it is a convention to use cls as the first parameter of a class method,
    #  similar to how we use self for instance methods.
    # class methods will change the value of class variable for all instances of the class, 
    # not just the instance that called the method.
    #  where as instance methods will change the value of class variable for the instance that called the method,(self)
    # class methods are defined using the @classmethod decorator, 
    # which is a built-in Python decorator that is used to define class methods.

    @classmethod
    def _change_var2(cls, new_value):   
        cls.var2 = new_value

# Static method is a function that have its own scope and does not have access 
# to the instance (self) or class (cls) variables.
    @staticmethod
    def static_method_example():
        print("This is a static method. It does not have access to the instance (self) or class (cls) variables.")

obj1 = MyClass()
print(f"Before changing var1 using instance method: {obj1.var1}")
obj1.change_var1('200')
print(f"After changing var1 using instance method: {obj1.var1}")
obj2 = MyClass()

# ---------------------------------------------------------------------------
print(f"Value of var1 in obj2: {obj2.var1}")  # Output: 200
print(f"Value of var2 in obj1: {obj1.var2}")  # Output: 500
print(f"Value of var2 in obj2: {obj2.var2}")  # Output: 500
obj1._change_var2('600')
print(f"Value of var2 in obj1 after changing with class method: {obj1.var2}")  # Output: 600
print(f"Value of var2 in obj2 after changing with class method: {obj2.var2}")  # Output: 600

# creating object of class for dunder method __str__ and calling it using print function
print(obj1)  # Output: This is the string representation of the object. var1
obj4 = MyClass()
print(obj4.__str__())  # Output: This is the string representation of the object. var1
print(obj4)