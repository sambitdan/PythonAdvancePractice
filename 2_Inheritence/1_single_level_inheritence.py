class Company:
    def __init__(self, company_name:str, location:str):
        self.company_name : str = company_name
        self.location : str= location

    def display_info(self):
        print(f"Company Name: {self.company_name}")
        print(f"Location: {self.location}")


# comp_obj = Company("Tech Solutions", "New York")
# comp_obj.display_info()

class Employee(Company):

    def __init__(self,employee_name,company_name,location):
        self.employee_name = employee_name
        self.company_name = company_name
        self.location = location


    def employee_info(self):
        response = Company.display_info(self)  # We can also use super() to call the parent class method
        print(f"Employee Name: {self.employee_name}, works at {self.company_name} located in {self.location}")




obj = Employee("John Doe", "Tech Solutions", "New York")
obj.employee_info()

