# Polymorphism where classes are different but function is same which increases the scalability of code. 
# We don't have to change the code everytime only change of class will suffice.

class api_fetch:
    def fetch(self):
        print('Printing data from API....')

class database_fetch :
    def fetch(self):
        print('Fetching Data from database')


class s3_fetch:
    def fetch(self):
        print('Fetching Data from s3 bucket ...')


obj = api_fetch()
obj.fetch()

obj = database_fetch()
obj.fetch()



