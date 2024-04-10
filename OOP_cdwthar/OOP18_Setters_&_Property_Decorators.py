
class Employee:
    email = 'bocchor.chocchor@ghidhora.com'
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@yahoo.com"

    def expalin_print(self):
        return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return f"Email isn't availble. Please set it using Setter.."
        return f"{self.fname}.{self.lname}@yahoo.com"
    
    @email.setter                 # make sure that during while making 'setter' type the 'method' name and then '.setter'
    def email(self, string):
        names = string.split('@')[0]
        f_l_name = names.split('.')
        self.fname = f_l_name[0]
        self.lname = f_l_name[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


Hindustani_supporter = Employee('Hindustani', 'Supporter')
nikkhil_pande = Employee('Nikkhil', 'Pande')

print(Hindustani_supporter.expalin_print())
print(Hindustani_supporter.email)

# now, let's say the Hindustani_supporter Employee or Object wants to change it's name into 'US supporter' 🥴🥴

Hindustani_supporter.fname = 'US'
print(Hindustani_supporter.email)


# now, say will it be worked? Absolutely not. Cause, 'lname' is Constructor and It's an Instance Attribute
# so, lname, fname cann't change the email Attribute



# now, if we want to Access the 'email' methods value without Calling as Function like: 'print(Hindustani_supporter.email())'
# then, we have to use '@property' Decorator look at the line 12 😎🙂

prin = Hindustani_supporter.email
# print(type(prin))
print(Hindustani_supporter.email)



# now, let's say we want to set Email and Want to Set also those Attributes which are included in Email. Here, we talking about the 'lname' and 'fname' 🙂🙂, let's see how.
Hindustani_supporter.email = 'this.that@yahoo.com'    # as the 'email' became a 'str' because of '@property' Decorator, so we can set it just like a 'str'

# but, yeah we meed to set 'setter' properly 😎 first. look at Line 16
print(Hindustani_supporter.email)
print(Hindustani_supporter.fname, Hindustani_supporter.lname)


# now, if we want to Delete email, then we have to set 'Deleter' at first..😎, like the 'setter'
# if we want to delete 'email' without setting 'Deleter' then it will return an AttributeError..

del Hindustani_supporter.email

print(Hindustani_supporter.email)