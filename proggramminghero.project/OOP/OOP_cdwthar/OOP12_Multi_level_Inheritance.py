class Electronic_Device:
    power = 'Lithium Battery'
    rechargeable = True
    var = 657

    def charging(self):
        self.var = 548
        print('We eat Electrons')
        print('cause, electrons are Yummy')

class Pocket_gadget(Electronic_Device):
    speciality = 'We are portable Device..!!'
    var = 87

    def mobile_phones(self):
        # self.var = 545887878787878
        print('We are the portable alternative of your PC')

class Phone(Pocket_gadget):
    camera = '10 Mega Pixel'
    battery = '7600 mh'
    OS = ['Android', 'iOS']
    internet = True
    var = 545

    def __init__(self, hey):
        self.var = 847
        self.hey = hey + ' are pocket gadgets'
        
    # var = 8
    def mobile_phones(self):
        # self.var = 547578
        print('We are the portable alternative of your PC')

my_mobile = Phone('We')
print(my_mobile.power)                                          # remember one thing that, always an 'Object' will check the 'attribute' firstly in
print(my_mobile.rechargeable)                                   # it's own 'Constructor Method or Any Method', if it will not be able to find there, then it will check that 
print(my_mobile.hey)                                            # at it's primary Parent Class's 'Constructor Method or Any Method', here that's 'Phone(Pocket_gadget)' class.  
my_mobile.charging()                                            # And if not then be found, then it will check at the it's Primary Parent Class's Parent Class, here which is the 'Electronic_Device' class. 
my_mobile.mobile_phones()                                       # if not then be found then it will come back to own Class and will search for 'Class Attribute' or 'Class Level Attribute' in it's own Class. 
print(my_mobile.speciality, my_mobile.OS, my_mobile.internet)   # if not found, then it will check in Primary Parent Class's 'Class Attribute'. 
print(my_mobile.var)                                            # if then not found again, then it will check in 'Primary Parent' Class's 'Parent Class'.




#   ||||||||||||||||||||||||||||||||||||||||||
