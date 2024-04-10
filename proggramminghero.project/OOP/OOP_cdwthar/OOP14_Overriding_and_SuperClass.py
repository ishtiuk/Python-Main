class A:
    classvar1 = "I'm a class variable in Class A"
    gd = 5

    def __init__(self):
        self.var1 = "I am inside of Class A's Constructor"

class C:
    classvar1 = "I'm a class variable in Class C"
    gd = 8

    def __init__(self):
        self.var1 = "I'm inside of Class C's Constructor"


class B(C, A):
    classvar1 = "I'm a class variable in Class B"

    # def __init__(self):                                          # if any same named 'Attribute' or 'Method' exist in both or all Classes 
    #     self.var1 = "I'm inside of Class B's Constructor"        # then those Attriubtes or Methods will be Overridden, 
                                                                    # for example, here the '__init__' method,
                                                                    # here class B's __init__ will be applied to the "als" Object.

                                                                    # that's why, Class B is the main own Class for 'als' Object,
                                                                    # so it will check it in 'Class B' first,    look at line 30 & 31
    def __init__(self):
        self.var1 = "I'm inside of Class B's Constructor"
        super().__init__()                   # but yeah, you can call the 'super class's __init__ after even overriden..!!!, like this    <<-------
        print(super().classvar1, super().gd)   # here, the 'Class A' is the Super Class for 'Class B and it's Objects, that's why it Inherited the Class A' at first.....
        
    # def __init__(self):
    #     self.var1 = "I'm inside of Class B's another Constructor"          # by the way, we can call any __init__ or any 'method' of any Parent Class like this, 
    #     # A.__init__(self)
    #     print(super().gd)
    #     print(C.gd)
                                          # So, now what is the difference of 'super() method or super().__init__()' and 'A.__init__(self)' method....?

                                         # Differences:: |||||||||||||

                                         # 1. 'super().__init__()' super method doesn't require to give 'self' as the first Parameter,
                                         #    on the other hand, 'A.__init__()' method requires 'self' as the first Parameter.

                                         # 2. 'super().__init()' super method can call only the Super Class which is the base Class or Firstly Inherited from 
                                         #    the Object's Class.   but on the other hand, 'A.__init__(self)' can call any Class which are the Praent Classes of 
                                         #    it's Object's Class.   For Example:
                                         #    here, 'super().__init__()' call only the 'Super Class' which is the 'Class C' here. But class A or C can be called 
                                         #    anytime using this: 'A.__init__(self) or C.__init__(self)', oh yea not only __init__ any othe Methods can be called
                                            
                                         #    remember, 'super().__init__()' calls only the Super Class, but any Class can be called like this: 'C.__init__(self)' 


a = A()                                                        
print(a.var1)
c = C()
print(c.var1,'\n')

als = B()
print(als.var1)



