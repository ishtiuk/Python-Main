
# Basically 'Dunder' Method is called the functions or methods which name starts with double underscore '__' and ends with double underscore '__' . Like    '__init__()' 

# yeah '__init__()' is also a Dunder method, this kinds of methods are automatically executed when making an Object using Class....


class C:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        # return self.salary * other.salary
        return f"I would not do division 😏, what you can do me? 😏"


    def __repr__(self):
        return f"I'm Class C"

    def __str__(self):
        return f"I'm powerfull that __repr__, when I will absent __repr__will come. Now, the time of me (__str___) 😏"

emp1 = C('Silver', 900)
emp2 = C('V', 500)

           

# if we want to do some Operator (+, -, %, *, /, //) etc mathmatical tasks with two Objects like sum, multi, divison, substraction etc
# then we can make special 'Dunder' methods inside the class to handle it..

# like if we give (+) between two Objects then program will find '__add__' method inside the Class if it's found then return the addtion or whatever we want to return from the Class

# if (/) between two Objects then program will find '__truediv__' method inside the Class

# if (//) between two Objects then program will find '__floordiv__' method inside the Class

# and vice versa...

print(emp1 + emp2)
print(emp1 / emp2)

# hence, we can return whatever we want from the Function 😏😏d

print(emp1 // emp2)




#  ||||||||||||||||||   __repr__   |||   __str__   ||\

# now if we want to print the 'emp' Object like print(emp)  then we'll see the Memory location of it, looks wired, so we can give it beauti help of '__repr__ and __str__ dunder method.. 😏

# but notice that when '__str__' isn't present then '__repr__' will be executed automatically, otherwise __str__ will execute first....

print(emp1)