# class Employee:
#     no_of_leaves = 6

#     def __init__(self, aname, aslaray, arole):
#         self.name = aname
#         self.salary = aslaray           # those Methods which starts with double underscore and ends with double underscore is called the Dunder Methods
#         self.role = arole               # so, init Method is also a Dunder Method
#                                         # 'Dunder Method' is a special kinds of Methods, which automatically runs or Executed when an Object are making.
#                                         # like here, 'emp1' was made the '__init__' Method automatically executed,
#                                         # that's why it's a Dunder Method  '😎😎😎
#     def print_details(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}"


# emp1 = Employee('Jhony', 500, 'Developer')
# emp2 = Employee('V', 85, 'Cleaner')

# try:
#     print(emp1 + emp2)                  # now, Class has got a 'Jatka'😂. That's Class doesn't know
# except:                                 # which which Attribute it should Add...
#     pass
#                                      # So to understand it to the Class we have to make a Special Dunder Method which will add the 'Salary' attribute of both Objects

# class Employee:
#     no_of_leaves = 6

#     def __init__(self, aname, aslaray, arole):
#         self.name = aname
#         self.salary = aslaray
#         self.role = arole  
    
#     def __add__(self, other):                       # notice that, the "methods or functions" names does matter here, like if you 'emp1 + emp2' at the Object, then it requires the '__add__' function inside the 'Class'.
                                                
#         return self.salary + other.salary
#         # return 'abcdef Whatever '                 # but, it doesn't matter that, what you will do inside the 'method or function', 
#         # return self.salary * othe.salary          # you can do anything inside it,:- that can be multiply, divison, sum, minus, print anything Whatever. 
#                                              # |||||||   But, always remember that, 'method or function' name should be 'appropriate'    |||||  
#                                              # let's disscuss more at Line - 50 - 52 , go below.....
#     def __truediv__(self, other):

#         return self.salary / other.salary
        
#     def __floordiv__(self, other):
        
#         return self.salary // other.salary

#     def __mul__(self, other):

#         return self.salary * other.salary

#     def __mod__(self, another):

#         return self.salary % another.salary

#     def __is_not__(self, other):

#         return self.salary is other.salary


#     def __repr__(self):
#         return f"Employee {self.salary, self.name, self.role}"

#     def __str__(self):
#         return f"The Name is {self.name}. Salary is ({self.salary} and Role is {self.role})"        # __str___ is powerfull when it's exist __repr__ will not automatically execute, hence we can call
#                                                                                                   # call repr, but if __str__ is absent then __repr__ will be executed automatically

# emp1 = Employee('Mokkel', 890, 'Sdkfj')
# emp2 = Employee('Jokkel', 45, 'kdjfdj')

# print(emp1 + emp2)          # whenever, you give here '+' Python will search the '__add__' named Dunder special MEthod inside the Class, 
#                             # if Python can found then it, then it'll return output, otherwise if Python can't find '__add__' method then it'll return Error
# print(emp1 / emp2)

# print(emp1 is not emp2)

# print(emp1 % emp2)

# print(emp1 * emp2)

# print(emp1 // emp2)

# print(emp1)
# print(emp2)


import requests
from bs4 import BeautifulSoup


d = requests.get('https://www.google.com/search?q=feniweathernow').text

html_data = BeautifulSoup(d, 'lxml')
print(html_data)
