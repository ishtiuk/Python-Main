
class Googler:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@google.com"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return f"Email isn't set. Please set it using Setter.."
        return f"{self.fname}.{self.lname}@google.com"

    @email.setter
    def email(self, string):
        names = string.split('@')[0]
        f_l_names = names.split('.')
        self.fname = f_l_names[0]
        self.lname = f_l_names[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
        


google_employee = Googler('google', 'Employee')
google_employee.fname = 'Microsoft'             # Though, we can override the 'fname' Instance Attribute from here, but it'll not effect the 'email' Instance Attribute' there, 
                                                # if we wannna change 'email' then we have to change that by Executing the 'Constructor' which is the '__init__' function, 
print(google_employee.fname)                    # but that's tiresome, right?
# print(google_employee.email)                    # 
                                                # so, let's be some lazy 😁, let's define a new 'Method' for 'email' only. 😁 Look at the, Line 10, 11 😉😏


# let's say the 'google_employee' want's to be 'microsoft employee' and wants to change it's 'email' through it's 'email' method by assinging email directly....
# but as, the 'email' is a Method, so we can't set it directly, like: """" google_employee.email = 'microsoft.Employee@google.com """"

# so, we need to convert the 'email' Method into a 'str', now, we have to use the '@property' Decorator to which will convert the 'email' Method into str..! 😃😃 
# look at the Line 12 .. 😏😏

print(google_employee.email, type(google_employee.email))  # as we can see that the 'email' isn't remain Method now, it's a stirng now..😎
# so, we can set 'email' now, because it's a 'string' <str> now

# but, we have to define a 'setter' Decorator inside the 'Class' to handle it, look at t
google_employee.email = 'microsoft.Employee@google.com'             # here, we can change our 'fname' and 'lname' Attribute too by setting just the 'email'.

print(google_employee.fname, '||', google_employee.lname, '||', google_employee.email)



# now, let's we want to Delete the 'email' so, we have to defince 'deleter' Decorator at the Above...🙂🙂

del google_employee.email

print(google_employee.email, '||', google_employee.fname,'||', google_employee.lname)

print(google_employee.email)




################               nOtice that  ###############

# when we want to access just the 'email' then Python will execute the 'email' named Method at the above at Line 10 and return the 'email'


# when we want to set the 'email' then Python will execute the '@email.setter attached email' method...... and it will set the 'fname', 'lname' and 'email' tooo..

# aaaaaand, when we want to Delete the 'email' then Python will execute the '@email.deleter attached email' 
# method and it will set 'lname' and 'fname' to None and 'email' will be vanished. 