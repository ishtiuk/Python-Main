

# let's make a Class,

class Phones:
    device_type = 'Mobile'                  # we have made a 'Phone' class for every types of Mobile phones. 


iPhones = Phones()                         # now, as a Mobile Phone 'iPhones' Object can get 'Phone' class's Attributes or Characteristics
Androids = Phones()                        # and, as a Mobile Phone, 'Androids' Object can also get 'Phone' class's Attributes or Characteristics


# now, iPhones and Androids made Debate among them, and got fired, mani bhejal

# so, they decided that they will make their own unsharable Attributes which is called the ' instance Attriubte ' , so let's see
iPhones.battery = 'short time usable'    
print(iPhones.battery)                  # so, '''  iPhones.battery = 'short time usable' ''' is only ' instance Attriubte' for iPhones, Androids can't use or access this

# so, Android also made own 'instance Attribute'

Androids.battery = 'long time usable'       
print(Androids.battery)                # so, ''' Androids.battery = 'long time usable' ''' is only ' instance Attriubte' for Androids, iPhones can't use or access this

print('\n\n')

# |||||||||||||   now, see Androids's battery Attriubte and iPhones's battery Attribute is only their own 'instance attribute' and own property, 
#   these won't be shared with each other, even in the 'Phones' class, that means if any other Objects can't also acess these Attributes, 
# because these are 'intance Attribute' can only own property,    Right?

# but the 'device_type' Attribute is availble for all Objects who uses the 'Phones' class, so it is avaible for 'Androids' and 'iPhones' both Objects
#      that's why,  'device_type' Attribute is a ' class attriubte ' or ' class level attriubte ', so each Object can use this



#  now, let's make some 'instance Attribute' using special kind of 'method' which is named 'def __init__(self)', which works to provide 'instance Attriubte' 

class Phones:
    device_type = 'Mobile'

    def __init__(self):     # <-- here, 'self' parameter is a changable parameter which automatically passes the 'Object' name as the value of 'self'
        self.OS = 'iOS'
        self.brand = 'Microsoft'
        self.RAM = '4 GB'

Androids = Phones()
iPhones = Phones()
Windows_phones = Phones()

print('device type: ', Androids.device_type,'\n', 'Operating System: ', Androids.OS,'\n', 'brand name: ', Androids.brand,'\n', 'Ram: ', Androids.RAM)
print('device type: ', iPhones.device_type,'\n', 'Operating System: ', iPhones.OS,'\n', 'brand name: ', iPhones.brand,'\n', 'Ram: ', iPhones.RAM)
print('device type: ', Windows_phones.device_type,'\n', 'Operating System: ', Windows_phones.OS,'\n', 'brand name: ', Windows_phones.brand,'\n', 'Ram: ', Androids.RAM)
#  now, as OS, brand, RAM is 'instance attribute' for all Objects so the all Objects can Holds the rights to change their own 'intance attriubtes', right?

# and moreover--->> Androids and Windows_phones got the 'iOS' Operating System and 'Microsoft' Brand and only '4 GB' RAM, 
# even Androids and Windows_phones has their own Operaing Systems and more RAMs.
#   ||||||||||||    so, that's not fair, Right?   |||||||   so, Androids and Windows_phones want to change their 'instance attributes' 
# and iPhones also want to change their 'brand name' from Microsoft to Apple. 🤣🤣

# so, let's see what we can do for these mobile phones


class Phones:
    device_type = 'Mobile'

    def __init__(self, OS_name, brand_name, RAMs):   #  __init__ method is called the 'Constructor', so this provides the 'instance attribute' to the Objects when
        self.OS = OS_name                            # when the Objects are making or contructing, (__init__) method doesn't needs to call, it automatically passed
        self.brand = brand_name                      # 'instance attributes' to the Objects, because it's the ' Constructor'  
        self.RAM = RAMs

Androids = Phones('Android 12', 'Samsung', '8 GB')      # and one moret thing 'Constructor' or the (__init__) method 🙂 allows to pass argument or parameter or value into the 'class' when making Objects
iPhones = Phones('iOS 14', 'Apple', '4 GB')             # 'class' when making Objects, here the ''' Androids = Phones('Android 12', 'Samsung', '8 GB')  '''
Windows_phones = Phones('Windows 10 / Windows 8', 'Microsoft', '6 GB')    # otherwise, you can't pass parameter or value or argument into the 'class' into the when making Objects   
                                                                        # by using any other 'method' 😏, only (__init__) method allows this, 
                                                                        # ok let me give you the proof about this in the last line😎😎

print('device type: ', Androids.device_type,'\n', 'Operating System: ', Androids.OS,'\n', 'brand name: ', Androids.brand,'\n', 'Ram: ', Androids.RAM)
print('device type: ', iPhones.device_type,'\n', 'Operating System: ', iPhones.OS,'\n', 'brand name: ', iPhones.brand,'\n', 'Ram: ', iPhones.RAM)
print('device type: ', Windows_phones.device_type,'\n', 'Operating System: ', Windows_phones.OS,'\n', 'brand name: ', Windows_phones.brand,'\n', 'Ram: ', Windows_phones.RAM)


class clas_to_give_proof:

    def prof(self, hello, nc):
        self.hello = hello
        self.nc = nc

try:      
    prroooff = clas_to_give_proof('nightcity', 'Cp77')
    print(prroooff.nc)
except TypeError as tpERR:                   #  as you can see that program returns an Error which is TypeError and that is
    print(tpERR)                           #  ''' clas_to_give_proof() takes no arguments ''', that means the 'clas_to_give_proof()' does not 
    pass                                  # takes arguments or parameter or value directly from the ' prroooff ' Object,
                                        # so directly arguments or parameter or value can take only the "Constructors" which is the '__init(self)' method 
                                        # and this supplys these values as 'instance attributes' to the all Objects which uses that 'class'
    
