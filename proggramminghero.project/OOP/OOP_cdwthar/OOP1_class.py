

# basically, 'class' is a template or blueprint which contains some specific 'attriubtes or characteristics' for it's the Objects which are using this class.

#   OOP means Object Oriented Progrmming, that means Objects will be the core-part of a specific program which uses the 'OOP'.

#  OOP follows the 'DRY' law, full form : Don't have to Relpy Yourself' .

# that means you do not need to declare or reply or define characteristics or attriubtes in every Objects, cause 'class' contains the attributes or characteristics,
# so, you can define Attributes or characteristics for an Object by just calling the 'class'

# let's declare or class or template:

class Student:
    pass                            #   notice that 'pass' keyword is used on Python to perform nothing, like it will not do anything..

jhony = Student()
silverhand = Student()              # here, is these two Objects are the same? Abosolutely not, let's test.. Run this program, you see that it will print this:
                                    # <__main__.Student object at 0x00000224424B7E50> <__main__.Student object at 0x00000224424B7DF0>

                                    # here, you can see these two Object are different, because it is allocated on different Memory location, 
                                    # the 'jhony' Object was stored in this: <__main__.Student object at 0x00000224424B7E50>  mermory location
                                    # on the other hand, the 'silverhand' Object was stored in this: <__main__.Student object at 0x00000224424B7DF0> mermory location.

print(jhony, silverhand)            # that means every Objects are different, even they have made by using same 'class' or attributes.


jhony.name = 'Jhony Samurai'           # hence, we can set an instance attribute from here like this, but it's not a good practise
print(jhony.name)                      # cause, Attributes should be declared or defined or seted inside the 'class'



# let's set some attribute from here for 'silverhand'

silverhand.subject = ['Arasaka', 'Computer']
print(silverhand.subject)               

# now, see if we want to print the 'silverhand.name' it will return error, because 'name' attribute was seted for 'jhony' only,
# even 'name' is not a 'class level attribute', that's why it's not availble for all the Objects which made from the Class.  
# 'class level attribute' is similarlly availble for all Objects and insider 'methods' (functions inside class)
# and one thing , 'class level attribute' should have declared inside the class and outside of every methods

try:
    print(silverhand.name)
except AttributeError as attrError:
    print(attrError)
    pass

# as you can see it had returned 'AttributeError', but we have handled that Error to continue the program.



#
    