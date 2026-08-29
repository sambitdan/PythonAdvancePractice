class Myclass:
# The variables defined inside the class are called attributes. We can access them using self.attribute_name.
#class variables are defined inside the class but outside any method. They are shared across all instances of the class.
    var1 = 'Hello World'
    var2 = 'Hello Python' 
    # Class variables are shared across all instances of the class. If we change the value of a class variable, 
    # it will change for all instances of the class. Instance variables are unique to each instance of the class. We can define instance variables 
    # inside the __init__ method, which is called when we create an instance of the class. 

#wWhenever we create a function inside a class, we need to pass self as the first parameter. This is because when we call the function, 
# it is called on an instance of the class, and self refers to that instance. We refer functions inside a class as methods.
    def func1(self):
        print(f"{self.var1}")

    def func2(self):
        print(f"{self.var2}")

#create an instance of the class(python object) and call the methods using the instance. We can also access the class variables using the instance.
obj = Myclass()
obj.func1()
obj.func2()