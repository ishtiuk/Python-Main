
class Shop_management_Structure_Software:

    def __init__(self, prducts_lst, product_X_price, product_with_Stock):
        self.products = prducts_lst
        self.products_price = product_X_price
        self.products_Stock = product_with_Stock
        self.customer_cart = []

        self.total_cost = 0


    def buy(self, product_nm, quantity):

        if product_nm in self.products and quantity <= self.products_Stock[product_nm]:            # here, we are maintaining the Stock Dict based on condition that if product in Stock Dict and Product nm List 🙂
            self.total_cost = self.products_price[product_nm] * quantity
            payment = int(input('Please pay '+str(self.total_cost)+' currency: '))

            if payment >= self.total_cost:
                self.products_Stock[product_nm] -= quantity
                self.customer_cart.append(product_nm)
                print('Sir, you got ', quantity, self.customer_cart)
                if payment > self.total_cost:
                    changes = payment - self.total_cost
                    print("Here's your return: ", changes)

        elif product_nm in self.products and quantity > self.products_Stock[product_nm]:
            print('''Sorry Sir, We this product is currently out of Stock!
            Please wait for 5 seconds''')
            self.restocker()

        elif product_nm not in self.products:
            print('Sorry, This product is currently unavailble!')

        self.customer_cart = []                             # after finishing shopping We wouldn't need to keep customers Product, so we are Emplying the 'cart' 😁


    def restocker(self):
        for products in self.products_Stock:
            crnt_stk = self.products_Stock[products]

            if crnt_stk == 0:
                self.products_Stock[products] += 15
                print('Restocking..! Stock Updated')


products = ['candy', 'chips', 'juice', 'Pizza', 'Burger', 'Cake']
products_price = {'Candy': 2, 'Chips': 10, 'Juice': 18, 'Pizza': 70, 'Burger': 30, 'Cake': 60}
products_stock = {'Candy': 0, 'Chips': 10, 'Juice': 20, 'Pizza': 25, 'Burger': 15, 'Cake': 5}

Arasaka_Shop = Shop_management_Structure_Software(products, products_price, products_stock)

# while True:
#     Arasaka_Shop.buy('Candy', int(input('Quantity: ')))


print(products_stock.lower())


# for products in products_stock:
#             crnt_stk = products_stock[products]                    # hightly analized intelliengence Algorithm to Restock Products depending on shortage. 😎
                                                                     # this ALGORITHM can realize the shortage by it's own and updates stocks by itself (kind of AI) 🤩

#             if crnt_stk == 0:                                      # and interesting thing is, this full Algorithm has analized, development and designed by myself own,
#                 products_stock[products] += 15                     # without Any help...... 🤩🤩🤩😎😎😎😎😎

                                                                     # I used this Algorithm on above in the 'def restocker(self)' MEthod to update Stocks 😎😎
# print(products_stock)