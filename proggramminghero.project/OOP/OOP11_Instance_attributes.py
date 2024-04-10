

#                            use __init__ to initialize Object attributes..



# Let's say you love shopping and you created a Shopping mall, now you need a class named 'Shopping'.

# In your Shopping class, you have a 'cart' attriubte and you have a method called 'add_to_cart'. Like below.....

class Shopping:
    cart = [ ] 
    def add_to_cart(self, item):
        self.cart.append(item)

#           now, on the weekend, you got a customer and that customer ordered a 'T-shirt' and the shopping cart looks like below...

class Shopping:
    cart = [ ]
    def add_to_cart(self, item):
        self.cart.append(item)

customer1 = Shopping()
customer1.add_to_cart('T-shirt')
# print(customer1.cart)

#          the next day, you got two customers. So, you created two customers from your Shopping class. Next, you wanted to see their cart and found something went wrong..
#       Can you spot why?

class Shopping:
    cart = []
    def add_to_cart(self, item):
        self.cart.append(item)

customer1 = Shopping()
customer1.add_to_cart('T-shirt')
print(customer1.cart)
customer2 = Shopping()
customer2.add_to_cart('Shoes')
print(customer2.cart)           #       so, here are the bug..!!! When you check the both customer's 'cart', 
                                #       you see that tge second customer's 'cart' has the 'T-shirt', even though he/ she didn't ordered or bought this...!

#               Mistake
#           here, this happend because the 'attribute' declared here the 'cart' attribute is a 'class level attribute'. These attribtes are shared among all the 
#    Objects created from the class.

#  That's why both the first and second customer was using the same level 'cart' list.


#               Instance Level

# To solve this problem, we have to create the 'cart' attribute inside the 'constructor'. Then, every Object from the Class will have a separate 'cart' attribute. 
# This is called an 'intance attribute', like below.......


class Shopping:
    def __init__(self):
        self.cart = [] 
    def add_to_cart(self, item):
        self.cart.append(item)

customer1 = Shopping()
customer1.add_to_cart('T-shirt')
print(customer1.cart)
customer2 = Shopping()
customer2.add_to_cart('Shoes')
print(customer2.cart)        


print(customer1)                # customer1 Atribute is located on this '<__main__.Shopping object at 0x000001D7078BDBB0>' memory location.
print(customer2)                # on the other hand, customer2 Attribute is located on this '<__main__.Shopping object at 0x000001D7078BDBE0>' memory location.