class Company:
    def __init__(self, company_name:str, location:str):
        self.company_name : str = company_name
        self.location : str= location

    def display_info(self):
        return f"Company Name: {self.company_name}, Location : {self.location}"

# comp_obj = Company("Tech Solutions", "New York")
# comp_obj.display_info()


class manager(Company):
    def __init__(self,manager_name : str , company_name : str, location : str):
        self.manager_name = manager_name
        self.company_name = company_name
        self.location = location

    def manager_info(self):
        response = Company.display_info(self)
        return f"The Manager : {self.manager_name} {response}"

class Employee(manager):

    def __init__(self,employee_name,manager_name,company_name,location):
        self.employee_name = employee_name
        self.company_name = company_name
        self.location = location
        self.manager_name = manager_name


    def employee_info(self):
        response = manager.manager_info(self)  # We can also use super() to call the parent class method
        print (f"Employee Name: {self.employee_name}, {response}")



# obj = Employee("John Doe", "Tech Solutions", "New York")
# obj.employee_info()
obj_2 = Employee('John Doe','James Smith',"Tech Solutions","New York")
obj_2.employee_info()
