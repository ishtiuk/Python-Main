
# A lot of the times you need to access an 'attribute' of an Object. To do so you will use the Object name, a dot, and name of the 'attribute'.

#       Example of accessing 'attribute' of an Object...
class Attibute:
    name = 'Algorithm'
    brand = 'Whatever'

attr = Attibute()
acess_attribute = attr.brand
print(acess_attribute)
print(attr.name)


# now, let's say, you want to set a new value to an 'attribute'. Ok, then Just write the 'attribute' on the left side. As if you are trying to access it.
# And write the new 'value' on the right-hand side, just like below......

#           Example of setting new value of any 'attribute'.

attr.name = 'HxD'
print(attr.name)            # as you can see that the 'name' Attribute has been changed..!!



# you can have as many 'attributes' as you want..  Like 'str' type, 'int' type, 'list', 'dictionary DS' etc types of 'attributes',       Like below....

#       Example of many kinds of Attributes....

class Many_knd_Attribute:
    brand = 'Samsung'
    price = 900
    apps = ['Programming Hero', 'Gmail']

new_attr = Many_knd_Attribute()
print(new_attr.apps)


#       Uppercase

# Usually, the name of the class starts with an UpperCase letter. You don't have to do it, but this is a convention. Pretty much every programmer does it.

#                   Multiple Objects
# From a Class, you can create as many Objects as you want.

class Multiple:
    dfkdj = 'fkldjf'
    dfkdj = 85656

multi1 = Multiple()
multi2 = Multiple()
multi3 = Multiple()

print("Quiz")
quiz = input('''\nWhich one is not True?
A. You can have as many Attributes as you want
B. You can create as many Objects as you want
C. You can create class only for electroincs : ''')

if quiz == 'C' or quiz == 'c':
    print('\nAbsolutely Right, Sir')

else:
    print('\nSorry, Sir. Wrong Answer')

#               Same Attribute

# All the Objects will have the same 'attribute'. However, the value of the 'attribute' does't have to be the same always. You can change it whenever.

#  remember, Every Object from a Class has the same Attributes.
