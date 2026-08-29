# Encapsulation is not a feature of Python, but it is a concept that is used to restrict access to certain attributes and methods of an object. 
# In Python, we can achieve encapsulation by using private and protected attributes and methods.

class Myclass:
    var1 = 'Hello World'
    var2 = 'Hello Python' 

    def __init__(self,dyn1,dyn2,dyn3):
        self.__dyn1=dyn1 # private attribute
        self._dyn2=dyn2 # protected attribute
        self.dyn3=dyn3 # public attribute

    def func1(self):
        print(f"Printing dyn1 : {self.__dyn1}")

    def func2(self):
        print(f"Printing dyn2 : {self._dyn2}")

    def func3(self):
        print(f"Printing dyn3 : {self.dyn3}")

obj = Myclass("Hello World from private attribute","Hello Python from protected attribute","Hello Python from public attribute")
obj.func1()
obj.func2()

obj.dyn1 = 'Hello World ' # we cannot access private attribute outside the class, it will give an error. 
# This is not changing the value of private attribute, it is creating a new attribute with the same name as private attribute.

print(f"Printing dyn1 : {obj.dyn1}") # we cannot access private attribute outside the class, it will give an error

obj.func1() # we can access private attribute inside the class using the method defined inside the class.

#Protected attributes can be accessed outside the class, but it is not recommended to do so. 
# It is a convention to use a single underscore before the attribute name to 
# indicate that it is protected and should not be accessed outside the class.
print(f"Printing dyn2 : {obj._dyn2}") # we can access protected attribute outside the class, but it is not recommended to do so.