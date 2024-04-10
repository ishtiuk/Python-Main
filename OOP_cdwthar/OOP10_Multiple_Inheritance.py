class Employee:
    no_pages = 75

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def khamakha(self):
        self.brand = 'Apple'
        return self.brand

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
Jhonny.alternative_of_constructor('Jhonny-650-Silverhand')

class Player:
    num_of_games = 54
    var = 3

    def __init__(self, xy):
        self.games = ['Tenis', 'Cricket']
        self.other_skills = 'Blog Writting'
        self.xy = xy

    def tpuye(self):
        self.type = "I'm a Player"

class all_rounder_Employee(Player, Employee):
    var = 779

    def tpuye(self):
        self.type = "I'm an allrounder employee"

    
goood_prog = all_rounder_Employee('hello')
pri = goood_prog.khamakha()    
print(goood_prog.khamakha())
print(goood_prog.printing_method('He'))
print(goood_prog.games)
print(goood_prog.xy)

try:
    print(goood_prog.name)              # __init__ has been overriden, because Class 'Player' has it's own __init__ or Constructor..
except AttributeError as attr:
    print(attr)
