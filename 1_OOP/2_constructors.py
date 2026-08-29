
#If we don't want to use default values provided by class owner, if we want to provide our own while creating an instance of the class (object creation), 
# we can use the constructor method __init__ to initialize the instance variables.
#  The __init__ method is called when we create an instance of the class. 
# We can define instance variables inside the __init__ method and assign values to them using self.attribute_name = value.

class Myclass:
    var1 = "Hello World"
    var2 = "Hello Python"

#Intance variables
    def __init__(self,dyn1,dyn2):
        self.dyn1=dyn1
        self.dyn2=dyn2

    def func1(self):
        print(f"Printing dyn1 : {self.dyn1}")

    def func2(self):
        print(f"Printing dyn2 : {self.dyn2}")


obj = Myclass("Hello World from instance variable","Hello Python from instance variable")
obj.func1()
obj.func2()

Myclass.func2(obj) # We can also call the method using the class name and passing the instance as an argument. This is called unbound method call.

# Whenever we call the class or create a object of the class, the __init__ method is called automatically while creating an instance of the class.
#  We can pass values to the __init__ method while creating an instance of the class.

obj_new = Myclass("Hello World from new instance variable","Hello Python from new instance variable")
obj_new.var2 = "Hello Python new" # We can also change the value of the instance variable after creating an instance of the class
print(f"Printing var2 from new instance variable : {obj_new.var2}")
