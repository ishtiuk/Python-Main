

# class Employee:
#     no_pages = 45

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
    
#                       # let's be some lazy, we don't want to give value separtely, like: ' jhony = Employee('Jhony', 800, 'Samurai') ',
#                                               # just imagine, we will give just 'stirng' and 'function' will set all value and distribute them by own..!!
#                                                 #   that's will be very amazing, Right?    ok, let's go to line number 20.........
       


# jhony = Employee('Jhony', 800, 'Samurai')
# silverhand = Employee('Silverhand', 500, 'Army')
# V = Employee('V-450-Surviour')                  # now, if you give a string directly, then it will return Error named TypeError, because here, takes 3 Arguments
                                                # but, we have given only this 'V-450-Surviour', which is only one Argument.. 🥴🥴



# for this, we have made the 'change_class_attr(cls, string)' method to Change class method Directly




class Employee:
    no_pages = 45

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_class_attr_from_slash(cls, string):
        params = string.split('-')
        # print(params)
        # print(type(params))
        # return cls(params[0], params[1], params[2])   # we can do this just in a one line
        return cls(*(string.split('-')))

    @classmethod
    def change_page(cls, para):
        cls.no_pages = para

V = Employee.change_class_attr_from_slash('V-135-Surviour')
Judy = Employee.change_class_attr_from_slash('Judy Avernce-230-Shopkepper')


print(V.name, V.salary, V.role)                     # now, we can change or set 'instance value or attribute' by using 'class Value changble method'
                                                    # as like as using the 'Consturctor method' which is '__init()__' function
print(Judy.name, Judy.salary, Judy.role)
# obj = Employee()
# print(obj.no_pages)



class Electronic_device:
    type = 'Electronic Device'
    power_source = 'Electric Source'

    def __init__(self):
        self.device_type = 'Electric'

    def our_descrip(self):
        print('We are the Electronic Devices')

class Pocket_Device(Electronic_device):
    portable = True
    power = 'DC Batttry'

    
class Mobile(Pocket_Device):
    Mobiles = 'SmartPhones'


    def our_advantages(self):
        print('We are the alternative of your PC')


android = Mobile()
print(android.device_type)


