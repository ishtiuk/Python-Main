
# All of the exceptions are the memeber of PYthon Base Execption class.

# when any exception occurs the Execption class returns an error Object, like NameError, TypeError, IndentationError, SyntaxError, etc..
# so, we have to handle this to keep our program or software running..

# like:

try:
    print(7 / 0)

except ZeroDivisionError as ZrrERR:    # we can also grab the Exception Object like this and use/ manipulate that. 
    print("Program has started")
    print(ZrrERR)

except:
    pass

else:
    print("No exception has occured...")   # if no exception has occured than 'else' statement or 'else' insider code will be executed...

finally:
    print("Program Complete")         # here, the "finally" keyword also performs like the "else" but, "else" will be executed if there will be no error.

    # but the "finally" will be executed always, doesn't matter there are Error or exception. Finally insider codes or statment will be executed always...



#   ||||||||||||||||||  Raise |||||||||||||

# we can return an error forcefully by using the 'raise' keyword. like below....


try:
    age = int(input('Enter your age: '))
    if age < 10:
        raise ValueError("Sorry, age restricted")
    else:
        print("Welcome")

except ValueError as e:
    print(e)
