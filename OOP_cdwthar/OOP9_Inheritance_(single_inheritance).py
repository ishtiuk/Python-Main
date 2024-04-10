class Employee:
    no_pages = 75

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_pages(cls, pages):
        cls.no_pages = pages

    @classmethod
    def alternative_of_constructor(cls, string):
        params = string.split('-')
        print(params)
        return cls(params[0], params[1], params[2])
        # return cls(*(params))
    @staticmethod
    def printing_method(str):
        print(str+' is very good person')

Jhonny = Employee('Jhonny', 500, 'Samurai')
print(Jhonny.no_pages)
Jhonny.change_pages(1055)
print(Jhonny.no_pages)
Jhonny.alternative_of_constructor('Jhonny-650-Silverhand')
print(Jhonny.name, Jhonny.salary, Jhonny.role)


class Programmer(Employee):
    no_of_vacation = 78

    def __init__(self, aname, asalary, arole, alanguages):

        Employee.__init__(self, aname, asalary, arole)
        self.languages = alanguages
        # super().__init__(aname, asalary, arole)

rohan = Programmer('Rohan', '876$', 'Sub Programmer', ['C++', 'Python'])

rohan.change_pages(899)
print('page number again changed:', rohan.no_pages)

Programmer.change_pages(5485)
Employee.change_pages('algodr')
Jhonny.change_pages('algorithom')
print(rohan.languages)

print(rohan.no_pages, rohan.no_of_vacation)

try:
    print(Jhonny.no_pages, Jhonny.no_of_vacation)
except AttributeError as atTrErR:
    print(atTrErR)


try:
    print(Programmer.languages)                # remember one thing always that, 'ClassAttriubtes' or 'Class level Attributes'
                                               # are directly accesable by both 'Class' name and 'Objects' those are made from that 'Class', 
                                               # but, remember that 'Initial Attributes' (Which are located inside the 'Constructor'
                                               # or the '__init()__' method, isn't directly accesable from 'Class'.
                                               # But yeah, it's accessable from Objects.                                             
except AttributeError as ATTrERRR:             
    print(ATTrERRR)



#           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#               |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
