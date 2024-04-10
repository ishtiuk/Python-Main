
#  


class Employee:
    num_of = 54

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_num(cls, now_num):
        cls.num_of = now_num

    @classmethod
    def from_str_chg_instance(cls, string):
        parasm = string.split('-')
        # return cls(parasm[0], parasm[1], parasm[2])
        # or 
        return cls(*string.split('-'))

    @staticmethod                        # let's make a Method which is needed no 'cls' or 'self' as the first parameter. And this Method will be independent, Let's say it'll do just printing...
    def printing_method(string):
        print(string + ' is a good person')

Joony = Employee.from_str_chg_instance('Jonny-5454-silver')
print(Joony.name, Joony.salary, Joony.role)
Judy = Employee.from_str_chg_instance('Judy-545-Shopholder')
print(Judy.name, Judy.salary, Judy.role)

print(Joony.printing_method('Jonny'))
Judy.printing_method('Judy')
