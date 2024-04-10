from abc import ABCMeta, abstractmethod
                                                # to declare Abstractmethod this step should be followed
class Shape(metaclass = ABCMeta):

    @abstractmethod
    def print_range(self):                      # 'AbrstractMethod' is a Decorator which Confirms that every Classes which are Inherited from Base Class have to must 
        return 0                                # contain the Abstracted Methods of the Base Class, 
                                                # for here that is the 'print_range()' Method.
                                                    
                                                # now, every Classes which are Inherited from this 'Shape' Base Class must to Contain 😎😎 a Method named 'print_area()', 
                                                # otherwise, it will return Error..!



                                                # and one most important thing that no Objects can be made by using directly the Abstract Base class,
                                                # here, the 'Shape' Class can't contain any Object, let's see ...🙂😎

try:
    shape_size = Shape()
except TypeError as typeERER:
    print(typeERER)


class Rectangle:
    type = 'Rectangle'
    sides = 4

    def __init__(self):
        self.length = 8
        self.width = 5
        
    def print_range(self):
        return self.length * self.width

class Triangle(Shape):
    type = 'Triangle'
    sides = 3

    def __init__(self):
        self.first_side = 5
        self.scnd_side = 5
        self.third_side = 5

class Circle(Shape):
    type = 'Circle'
    sides = 'all'

    def __init__(self):
        self.pai = 3.1416
        self.radius = 8

    def print_range(self):
        return self.pai * (self.radius ** 2)


circle1 = Circle()
print(circle1.type)



