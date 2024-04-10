class Shopping:
    def __init__(self):
        self.total = 0
        self.cart = []
    def add_to_cart (self, item, price):
        self.cart.append(item)
        self.total = self.total + price
    def checkout(self, amount):
        if amount != self.total:
            print('No Change')
            print('Please pay Exact Amount', self.total)
        else:
            print('Thanks for wasting money!')
            print('You got', self.cart)
            self.total = 0
            self.cart = []
           
my = Shopping()
my.add_to_cart('T-shirt', 40)
my.checkout(40)



# this Software is ordinary and it's smells some wired to me. fuck up,

# I can make better than it 😏 , check 'E_Commerce_Software_by_me.py' 😎
