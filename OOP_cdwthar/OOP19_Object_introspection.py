
# now, Remember onething that Everything in "Python Programming" is remains as an Object like: int type varrible is 'int' Object
#  def is 'function' Object, sting type varrible is 'str' Object etc...

from pandas.io.parquet import to_parquet


a = 8
b = 15.2
c = 'hello'

def helo():
    pass

print(type(a), type(b), type(c), type(helo))

#    so, now what is Object Instrospection?  IT's just a way to Know about any 'Object' in details.... that's it

class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@gmail.com"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return f"Please set Email, using Setter"
        return f"{self.fname}.{self.lname}@gmail.com"
    
    @email.setter
    def email(self, stirng):
        names = stirng.split('@') [0]
        f_l_name = names.split('.')
        self.fname = f_l_name[0]
        self.lname = f_l_name[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

google_employee = Employee('google', 'employee')
print(google_employee.email)

google_employee.email = 'microsoft.employee@gmail.com'
print(google_employee.email)

del google_employee.email

print(google_employee.email)



#   now, let's try Instrospection on the 'Employee' Class 😎😎

# some introspection ways:
# 1. type
# 2. id
# 3. dir

# print(type(Employee))
# print(id(Employee))
# print(dir(Employee))


# import inspect

# print(inspect.getmembers(Employee))

# print(inspect.getmembers(google_employee))
