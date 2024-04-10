
# now, what is the usage of  'self' parameter in method?

# let's say, you have a bank account.

# now, you want to create a 'method' named get_balance. From that method, you want to return the accont balance.

# Access Attribute using 'self' parameter.

# Use the 'self' parameter to access any attributes of the class from inside a method. Just use 'self' and then a dot '  .  ' sign and then name of the attribute. like below...



#                   'self' parameter is necessary to access any 'attributes' or any another 'methods' from a 'method', that's all........



class Bank:
    account_balance = 1000
    def get_balance(self):
        return self.account_balance

my_account = Bank()
balance = my_account.get_balance()
print(balance)

# usage of 'self' parameter to 
# access Everything.......

# Let's say you have multiple attributes. You can access every attributes by using self, dot sign "  .  " and the name of attribute. like below.....
class Bank:
    account_balance = 2000
    account_owner = 'Silverhand'
    bank = 'Arasaka International Bank'

    def bank_details(self):
        ac_bal = self.account_balance + 10
        ac_ow = "Jhony"
        bnk = self.bank.replace('Bank', '')
        return self.account_balance, self.account_owner, self.bank, ac_bal, ac_ow, bnk

my_bnk_details = Bank()
baln = my_bnk_details.bank_details()
print(baln)


# 'self' parameter usage to 
# access 'Methods'

class accessing_methods:
    
    def first_method(self):          # remember that here you have to give one parameter must, 
        return 'first method'        # but it's not essantial to give the name of the parameter 'self'. you can name it anything like, 'dflkdfkd'.
         
    def second_method(self):
        return 'second method', self.first_method()

acessing_method = accessing_methods()
accesses = acessing_method.second_method()
print(accesses)

print('Quiz')
quiz = input('''What is the purpose of the 'self' parameter?
A. To acess class Attriubtes
B. To acess class Methods
C. All the above :: ''')

if quiz == 'C' or quiz == 'c':
    print('\nabosolutely Right, Sir')

else:
    print('\nsorry, Sir. Wrong answer')

#           use the 'self' parameter to access 'attributes' and 'methods'.





#
