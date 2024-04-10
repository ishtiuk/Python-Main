
class Employee:
    no_of_leaves = 0

    def printdetails(self): 
                                # <-- here, 'self' parameter is a changable parameter which automatically passes the Object's name as the value of 'self'
        return 'hello'          # according to which Object calls the 'method', now, if we say that  'silverhand' Object calls the 'method' like this at below

                                 # silverhand = Employee()
                                 # silverhand.printdetails()
silverhand = Employee()
print(silverhand.printdetails())    # here, as we calling 'printdetails()' method by typing 'silverhand.printdetails()',
                                    # so 'silverhand' has automatically passed as the value of 'self' in the 'printdetails(self)' method



#  now let's see if we don't give 'self' as the first parameter in a 'method', what will be happened now?

class hXd_employee:
    employee_num = 10

    def all():        # <-- notice that, we have not given 'self' parameter here, thought it's essatial, let's see what will happen?
        return 'we are hXd engeneers'

try:                         # as we can see that this 'programs' throws an Error named TypeError and that is-->
    jhoney = hXd_employee()     # "  all() takes 0 positional arguments but 1 was given   ", 
    print(jhoney.all())        # that means || When we called that 'all()' method on the 'jhony' Object then it has passed 'jhony' into the 'all()' method as a parameter automatically,
                           # so we have to handle the 'jhony' parameter. 
                           # |||||||  NOw, we must have to give 'self' as the first parameter in a 'method' to handle this situation. |||| 
                                                      
except TypeError as typErr:
    print(typErr)               # here, program throws an Error which is TypeError, so we used try except to save program from crashing.....


    