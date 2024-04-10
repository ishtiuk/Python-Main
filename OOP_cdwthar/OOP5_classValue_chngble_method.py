

# now, what is 'class value changable method?'

# we, have saw '__init()__' method, and various method, which are used to change 'Object' values

# but, did you think about that, How to change Class value using a 'method'? Ok, let's see

class System_al:
    naem = 'hello'

    def __init__(self):
        self.had = 7
        
    def change_object_value_or_attriubte(self, hd):
        self.had = hd

sys = System_al()

print(sys.had)              # here, is the value of 'had' instance attribute for 'sys' Object, 
sys.change_object_value_or_attriubte(8787)        # we can override or change the 'had' attribute's value by calling the 'change_object_value_or_attriubte()' method, Right? 
print(sys.had)
# that's very simple

# we can also change the 'class level attriubte' for Object or even can change 'class level attriubte' for Whole Class...!! , like below:
#          ||'class level attriubte' change for Object||     
sys.naem = 'welcome to nightcity'
print(sys.naem)  
print(System_al.naem)   # here, Class's  'naem' attribute's value hadn't changed, but we can also change that like below.

#         ||'class level attriubte' for Whole Class...!!
System_al.naem = 'all changed! smasher'
print(System_al.naem)          # now, 'neam' attribute's is changed for whole class.


# now, this is boring to change to Class for Whole class by declaring '  System_al.naem = 'all changed! smasher' ' again and agian, Right?

# so, let's make a 'method' to change Whole Class's Attriubte...!!


class Syst:
    namId = 6544
    IMeI = 5454544

    @classmethod                                # @classmethod is a Decorator, more things explaination about 'Decorator' is located in this directory:  
                                                #"D:\pip main\proggramminghero.project\OOP\OOP_cdwthar\OOP5_classValue_chngble_method.py"
                                                
    def change_cls_attribute(cls, nmID, imEI):  # here, first paramete is 'cls' not 'self' because we want to change and play with 'class level attributes' 😎😎    |||
        cls.namId = nmID
        cls.IMeI = imEI

systing = Syst()
print(systing.change_cls_attribute(554, 54545))
print(systing.namId, systing.IMeI)
print(Syst.namId, Syst.IMeI)                # as you can see that, class attributes 'namId' & 'IMeI' has fully changed...!! 😎😎😏   ||