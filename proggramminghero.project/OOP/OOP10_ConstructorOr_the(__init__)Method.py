

#               Initial Values

# While creating the 'class', you can provide initial values. 


#              Constructor

# those initial values are provided via a special method. As a convention, most of the programming languages call it the 'constructor'. 
# For simplicity, we will call it 'Constructor' as well.


#              Underscores
# In the Python programming language, the 'constructor' method has to have a spcial name that is '__init__', it's two underscores, then init, and two underscores more... like below..
 
class Phone:
    def __init__(self, brand):
        self.brand = brand

my_phone = Phone('Samsung')

grandma_phone = Phone('NOKIA 1100')

print(my_phone.brand)
print(grandma_phone.brand)


#           Automatic

# While creating an Object, you will not explicitly call the '__init__' method. Instead, python will automatically call it at the time of creating a new object. 

# However, in some advanced cases, you might call the '__init__' method directly.


#           Object Attribute

# inside the '__init__' method you can just write the attribute name after the 'self' parameter. Python will add that 'attribute' to the Object created by the 'constructor'.

# It's okay to be confused. It's part of learning process. Keep moving forward things will be better and easier. I promise.


#                   Just pass Params (parameters)

# All you have to do is to pass the parameters while creating a Object. Exclude the self parameter. for example below..

class Laptop:
    def __init__(self, brnd):
        self.brand = brnd          # here the name of the Atrribute of 'self.brand' is not essential, it can be anything, like 'self.abc', because it just creating
                                   # a new attriubte the 'brand' parameter will be the value of the 'self.brand' attribute. and the 'brand' parameter will be taken
        self.age = 10              # from the Object calling named 'lap = Laptop('HP')', print()
        

    def add_year(self, increment):
        self.age = self.age + increment

lap = Laptop('HP')
print(lap.brand, lap.age)
lap.add_year(5)
print(lap.age)


quiz = input('''\nWhat is the purpose of the __init__ method?
A. To initialize object instance attibutes
B. To initialize a video chat with python
C. Practice quick typing of underscores :: ''')

if quiz == 'A' or quiz == 'a':
    print('Absoluetly Right Answer, Sir..!!')
else:
    print('Sorry, Sir. Wrong Answer')


# use __init__ to initialize Object attributes..