
class Coffee_Supplier_at_Bulk:
    devlopers = 's_il_ver_ha_nd'

    def __init__(self, stock):
        self.max_stock = stock
        self.sold = 0
        self.__cost_or_income = 0


    def order_coffee(self, quantity):
        if quantity <= self.max_stock:
            self.__cost_or_income = quantity * 15
            pay = float(input('Please pay '+str(self.__cost_or_income)+' currency: '))
            if pay == self.__cost_or_income:
                self.sold = self.sold + quantity * 4.5
                self.max_stock -= quantity
                print('Thanks for buying Coffee')

            else:
                print('Sorry, Sir. Not sufficient currency.\nPlease pay exact '+str(self.__cost_or_income)+' currency')

        elif quantity > self.__cost_or_income:
            print('''Sorry, Sir! We are out of stock.
            Please come after 5 second. We are restocking!''')        
            self.restok_coffee()                                 # here, I have learnt a new thing. 🤩,  
            self.khamakhe()                                                     # that's any Method or Fuction can be called before assigning in Class
                                                                 # but, remember is only works in Class, not for Ordinary Functions 🥴, look at the last lines...
        else:
            print('Unexpected ErRor')
        

    def restok_coffee(self):
        self.max_stock += 100
        print('''Restocked. Stock Updated!
        You can place order now!''')
    
Coffee_Shop = Coffee_Supplier_at_Bulk(150)

def UI():
    usr_inpu = input('''
    |==== Enter 'O' to order or buy ===|
    |====   Enter 'X' to Exit   ===|
    :->> ''').upper()

    if usr_inpu == 'O':
        Coffee_Shop.order_coffee(int(input('Enter Coffee Quantity: ')))
    if usr_inpu == 'X':
        exit()


while True:
    UI()


print()
print()
def hello():
    print('Board')

try:
    khamakha()
except NameError as nmERr:                                            # it have thorwn a 'NameError' that 'khamakha()' function isn't defined. 
    print(nmERr)                                                      # so, remember that calling Method or Function before assignment only works in Class 🙂 in OOP.

def khamakha():
    print('hey')