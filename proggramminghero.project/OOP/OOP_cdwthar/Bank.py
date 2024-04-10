
class Bank_ac:
    Bank_name = 'Swiss Bank'


    def __init__(self):
        self.__balance = 84700


    def deposit(self, amount_of_depo):
        self.__balance += amount_of_depo
        print('You have successfully deposited:', amount_of_depo, ', Sir')
        print('Now your current balance is:', self.__balance, ', Sir')


    def withdraw(self, withdrawal):

        if withdrawal <= self.__balance:
            self.__balance -= withdrawal
            print('You have successfully withdrew:', withdrawal, ', Sir')
        else:
            print('Sorry, Sir. You have not sufficient balance')
        print('Your current balance is:', self.__balance)

    def check_balance(self):
        print('Your current balance is:', self.__balance)


    @staticmethod
    def wishing():
        print("Thanks for staying with Swiss Bank, Sir")


ac_holder = Bank_ac()
ac_holder.check_balance()

try:
    print(ac_holder.__balance)
except AttributeError as attrERR:
    print(attrERR)

ac_holder.deposit(782)
ac_holder.withdraw(0.25)
ac_holder.check_balance()
ac_holder.wishing()

                                        # but, I have a secret way to Access Private attibute, which is '__balance' directly from 'Object'..😎😎
print(ac_holder._Bank_ac__balance)