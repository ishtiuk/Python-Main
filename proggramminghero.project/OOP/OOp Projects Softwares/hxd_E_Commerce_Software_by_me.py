
class E_Commmerce_Soft_Structure:

    def __init__(self, product_price_lst, product_lst):
        self.product_price_lst = product_price_lst
        self.product_lst = product_lst
        self.total_cost = 0
        self.cart = []


    def add_to_cart(self, item):
        if item in self.product_lst:
            price = self.product_price_lst[item]
            self.total_cost = self.total_cost + price

            itm_indx = self.product_lst.index(item)
            itm = self.product_lst.pop(itm_indx)
            self.cart.append(itm)
            print('Successfully added '+ itm + ' to your cart')
            
        elif item not in self.product_lst:
            print('Sorry, Sir. This item is currently unavailbe')


    def check_out(self, payment):
        # for product in self.cart:
        #     self.total_cost += self.product_price_lst[product]                | this is not applicable, because this Adds prices thought product isn't buying , 
        # print(self.total_cost)                                                | alternative Algorithm has given to 'add_to_cart()' method to count prices 😎
        if payment >= self.total_cost:
            print('Successfully paid, Sir')
            print('Here are your goods: ', self.cart)
                                                 
            print(self.total_cost)
            if payment > self.total_cost:
                changes = payment - self.total_cost
                print('Here is your changes:', changes)
            
        elif payment < self.total_cost:
            print('Sorry, Sir. No changes')
            print('Please pay the extact payment')

            while payment != self.total_cost:
                print('Please pay exact: ', self.total_cost)
                pay = float(input('Payment: '))
                if pay == self.total_cost:
                    print('Successfully paid, Sir')
                    print('Here are your goods: ', self.cart) 
                    break

        else:
            print('Unexpected ERror')

        self.cart = []  
        self.total_cost = 0 

    def display_items_and_prices(self):
        for key in self.product_price_lst:
        # for key in self.products_prcs_lst.keys():                     # it will do also same thing 😎
            price = self.product_price_lst[key]
            print(key, 'price is:', price)

    @staticmethod
    def thanking():
        print('|== Thanks for coming, Sir. Have a nice day ==|')


products_prcs_lst = {'T-SHIRT': 420, 'SHIRT': 500, 'JEANS' : 541, 'SCHOOL BAG': 962}
products = ['T-SHIRT', 'SHIRT', 'JEANS', 'SCHOOL BAG']
Araska_Online_Shop = E_Commmerce_Soft_Structure(products_prcs_lst, products)

def UI():
    user_input = input('''
    |====    Enter 'D' to see Products   ====|
    |====        Enter 'B' to Buy        ====|
    |====    Enter 'F' end of Shopping   ====|
    |====        Enter 'X' to Exit       ====|
    :->> ''').upper()

    if user_input == 'D':
        Araska_Online_Shop.display_items_and_prices()
    elif user_input == 'B':
        Araska_Online_Shop.add_to_cart(input('Product Name: ').upper())
    elif user_input == 'F':
        Araska_Online_Shop.check_out(float(input('Payment: ')))
    if user_input == 'X':
        Araska_Online_Shop.thanking()


while True:
    UI()