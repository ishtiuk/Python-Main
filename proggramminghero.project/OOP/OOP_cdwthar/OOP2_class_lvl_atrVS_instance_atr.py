

# basically, those 'attributes' or 'varibles' which are declared in a 'class' are called the 'class attriubte' or 'class level attribute', 
# remember those should be declared outside of every 'method'

class Apple:
    phn_type = 'iPhone'          # here, the 'phn_type' attribute is 'Apple' class's property only, 
    tab_type = 'iPad'            # this will be shared Equally among those Objects which are made by using this 'Apple' class.
    pass                           

    
iPhone5 = Apple()           # now, iPhone5 Object was made by using this template or class named Apple. 
                            # So, iPhone5 Object has gained it's type which is 'iPhone' using the 'phn_type' attribute (class attriubte/ it is class level attribute/)

iPhone13 = Apple()          # similarly, iPhone13 Object also made by using this template or class named Apple.
                            # So, iPhone13 Object has also gained it's type which is 'iPhone' using the 'phn_type' attribute (it is class level attribute)


iPhone13.display_resolution = '1170 x 2532'            # here, 'display_resolution' is 'instance' Attribute and it's only iPhone13's property.
                                                    # it will not be shared with other Objects.
print(iPhone13.display_resolution)

iPhone5.display_resol = '640x1136'            # and here, 'display_resol' is another 'instance' Attribute and it's only iPhone5's property.
                                              # it also will not be shared with other Objects.
print(iPhone5.display_resol)

#     all of the above these two 'instance' attributes of iPhone5 and iPhone13 is unique and only their own property. 
#     these 'instance' Attributes of iPhone5 and iPhone13 has no connection with each other and also have no connection with the 'Apple' class too, 
#     that's why these are 'instance attribute'


# but here, the 'phn_type' Attribute is 'class attriubte' or 'class level attribute', so it should be equally shared to all Objects which uses this 'Apple' class, Right?
# So, both Objects named 'iPhone5' & 'iPhone13' has gained the Attribute named 'phn_type', So, let's seee....

print("it's an",iPhone5.phn_type)
print("it also an", iPhone13.phn_type)      # so, these all are iPhones


#      now, can these iPhones are convert them into Android?  just fun, 
#    actually I want to say that can these iPhone5 and iPhone13 (Objects) can change the '''  'class attribute's value of "Apple" class?''' which is 'phn_type'
# abosolutely, not because this 'phn_type' Attribute is only 'Apple' class's property.  

#              |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#   ||||||||||||||||||||||||||||||||||||||||||||||||

iPhone5.phn_type = 'Android'                # products can change own attributes so, iPhone5 changed itself into 'Android', 
print(iPhone5.phn_type)

  #      but Company 'Apple' class's value remains same

print(Apple.phn_type)


#      hence,   class which is 'Apple' can change is own property here the 'phn_type', but those any Object can't change 'class' value or attrbute

Apple.phn_type = 'Harmony OS Phone'             # now, Company 'Apple' class has decided to changed it's own 'phn_type' into 'Harmony OS Phone'
print(Apple.phn_type)
print(iPhone13.phn_type)

#  and obiously, a Company can change it's own property, but the products of those Company can't change Company's value of property, Right?  
#    products can change their own property or value or attribute.

# here Company is Apple class
# and products are iPhone5 and iPhone13


#       ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#   so, we have learnt about the difference between the 'class Attribute'/ 'class level Attribute' and 'instance Attribute'


#  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||





#  