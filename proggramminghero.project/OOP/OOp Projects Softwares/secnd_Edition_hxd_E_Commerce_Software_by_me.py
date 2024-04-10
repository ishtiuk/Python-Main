
class E_Commerce_Software:

    def __init__(self, product_prices, product_lst):
        self.product_prices = product_prices
        self.product_lst = product_lst
        self.cart = []
        self.total_price = 0

    def add_to_cart(self, item):
        if item in self.product_lst:
            price = self.product_prices[item]
            self.total_price = self.total_price + price

            itm_indx = self.product_lst.index(item)
            itm = self.product_lst.pop(itm_indx)
            self.cart.append(itm)
            print(itm, 'added to your cart')
        
        elif item not in self.product_lst:
            print('Sorry, Sir. This product is currently unavailble')

    def check_out(self, total_payment):
        if total_payment >= self.total_price:
            print('Payment Successful, Sir')
            print('You got: ', self.cart)
            if total_payment > self.total_price:
                cash_back = total_payment - self.total_price
                print("Here's your returns: ", cash_back)
        
        elif total_payment < self.total_price:
            print('Sorry Sir, no changes')
            print('Please pay exact amount: ', self.total_price,'\nand try again!')

        self.total_price = 0
        self.cart = []

    def display_items_and_prices(self):
        for key in self.product_prices:
        # for key in self.products_prcs_lst.keys():                     # it will do also same thing 😎
            price = self.product_prices[key]
            print(key, 'price is:', price)

    @staticmethod
    def thanking():
        print('\n|== Thanks for coming, Sir. Have a nice day ==|\n')


products_prcs_lst = {'T-SHIRT': 420, 'SHIRT': 500, 'JEANS' : 541, 'SCHOOL BAG': 962}
products = ['T-SHIRT', 'SHIRT', 'JEANS', 'SCHOOL BAG']
Araska_Online_Shop = E_Commerce_Software(products_prcs_lst, products)


def UI():
    user_input = input('''
    |====    Enter 'D' to see Products   ====|
    |====        Enter 'B' to Buy        ====|
    |====    Enter 'F' end of Shopping   ====|
    |====    Enter 'P' to pay currency   ====|
    |====        Enter 'X' to Exit       ====|
    :->> ''').upper()

    if user_input == 'D':
        Araska_Online_Shop.display_items_and_prices()
    elif user_input == 'B':
        Araska_Online_Shop.add_to_cart(input('Product Name: ').upper())
    elif user_input == 'F':
        print('Please pay', Araska_Online_Shop.total_price, 'currency, Sir')
        Araska_Online_Shop.check_out(float(input('Payment: ')))
    elif user_input == 'P':
        print('Please pay', Araska_Online_Shop.total_price, 'currency, Sir')
        Araska_Online_Shop.check_out(float(input('Payment: ')))
    if user_input == 'X':
        Araska_Online_Shop.thanking()
        exit()

while True:
    UI()