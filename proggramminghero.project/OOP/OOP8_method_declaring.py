
#   Declaring a method is very simple.

# You just declare a function inside the class. For example, you have the Phone class. Now you are adding the 'hard_work' method.

# Example of Declaring a 'method':

class Phone:
    company = 'Arasaka'
    
    def company_name(self):
        print('Araska Nightcity')

#   Notice that, it's just a simple function inside the class. However, you have to provide one parameter always here.....! You may or may not use this parameter. Usually, this parameter is called
#  'self'.


#           Call a Method 
# To call a method from a 'class'. You will just create an Object. Write the Object name and then a dot and then call the 'method' as if you are calling a function..🙂.
# Also, note that you won't pass the first parameter. Python will do it for you. 

# Don't get confused. Keep going. This will make sense later, I will explain more.

class Phone:
    company = 'Arasaka'
    
    def company_name(self):
        print('Araska Nightcity')
        
    
my_com = Phone()
my_com.company_name()


#       Parameters
# If you want to pass one or more parameters to a 'method'. Then you will write those parameters after the the 'self' parameter. Below, we have a method named add a for a Calculator.

class Calculator:
    brand = 'Casio'
    def add (self, a, b):
        return a + b

#  while calling the 'method', you will pass all the parameters excluding the 'self' parameter.
# Python will automatically pass the 'self' parameter.

my_calc = Calculator()
my_calc.add(2, 3)


# Methods are like functions. You can store method output to a variable and use it for other purposes. Like the deduct function below. 

class Calculator:
    brand = 'Casio'
    def add (self, a, b):
        return a - b

my_calc = Calculator()
result = my_calc.add(8, 5)
print(result)


print('Quiz\n')

quiz1 = input('''What would be the first parameter of the multiply method?
class Calculator:
    brand = "Canon"

    def multiply (______, a, b):
        return a * b
        
my_calc = Calculator()
result = my_calc.multiply (5, 7)
print(result) :: ''')


if quiz1 == 'self':
    print('\nabsolutely Right, Sir\n')
else:
    print('\nsorry, Sir. Wrong answer\n')


#  The first parameter of a method will be 'self'.