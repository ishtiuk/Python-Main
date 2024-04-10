class Employee:
    no_of_leaves = 6

    def __init__(self, aname, aslaray, arole):
        self.name = aname
        self.salary = aslaray
        self.role = arole  
    
    def __add__(self, other):                       # notice that, the "methods or functions" names does matter here, like if you 'emp1 + emp2' at the Object, then it requires the '__add__' function inside the 'Class'.
                                                
        return self.salary + other.salary

    def print_details(self):

        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}"


    def __repr__(self):
        return f"Employee {self.salary, self.name, self.role}"

    def __str__(self):
        return f"The Name is {self.name}. Salary is ({self.salary} and Role is {self.role})"
        # return self.print_details()


emp1 = Employee('Out', 85, 'Over')

print(emp1)     # before defining '__repr__' or '__str__' named Special Dunder Method it'll return memory location <__main__.Employee object at 0x0000012285487CA0>.

                # but, if we want to return some meaning full thing with this stupid line 'print(emp1)', then we can define '__repr__' or '__str__' Methods inside the Class.

        #           now, '__repr__'    VS    '__str__' Dunder Special Method  😎😎

        #       1. here, '__str__' is Powerfull, 😎😎 that's why, if '__str__' is exist in the Class Python will execute the '__str__' first and it will not execute the '__str__'. 
        #       2. and, if we want to execute the '__repr__' Method despite there exist '__str__' then, we have to call '__str__' specifically, 
        #          like the Line 47 .. look below.. 
        #       3. Remember that, if the '__str__' exist in the Class then it wil get the 'Privilege' 😎😎😏....!!! ,
        #          if we call it or not call it Python will execute '__str__' by-default. .. 😎😎


        #       4. Annnnnnnnnnd, if the Boss which is '__str__' doesn't exist but '__repr__' exist then thought we type 'print(str(emp1))', 
        #          then Python will execute '__repr__', cause the Boss 😎😏 '__str__' doesn't exits there.... |||   look at Line:  73

print(str(emp1))

print(repr(emp1))


class Employee:
    no_of_leaves = 6

    def __init__(self, aname, aslaray, arole):
        self.name = aname
        self.salary = aslaray
        self.role = arole  
    
    def __add__(self, other):                       
                                                
        return self.salary + other.salary

    def print_details(self):

        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}"


    def __repr__(self):
        return f"Employee {self.salary, self.name, self.role}"


emp1 = Employee('Hello', 54, 'Wind')

print(str(emp1))