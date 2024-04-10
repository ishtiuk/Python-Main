import random

string = 'AaBbCXxYyZzcDdEeFfGgJjKkLMmNnOoPHhIipQqRrSsTtUuVvWw'
symbols = '+(&%|,A$!~}i<-?>/'
print(len(symbols))

random_pass = ''

def random_password(type):
    num1 = str(random.randint(0,99))
    num2 = str(random.randint(0,9))

    alpha1 = string[random.randint(0,50)]
    alpha2 = string[random.randint(20,40)]
    alpha3 = string[random.randint(13,25)]
    alpha4 = string[random.randint(31,45)]

    symbol1 = symbols[random.randint(0,15)]
    symbol2 = symbols[random.randint(5,10)]
    symbol3 = symbols[random.randint(9,15)]

    if type == '1' or type == 'easy' or type == 'normal':
        random_password = num2 + symbol2 + alpha4 + num1 + alpha1 + alpha2
        return random_password
    elif type == '2' or type == 'medium' or type == 'intermidiate':
        random_password = alpha1 + alpha2 + symbol1 + alpha3 + symbol2 + num1 + alpha2 + num1 + alpha3
        return random_password
    elif type == '3' or type == 'hard':
        random_password = alpha1 + num2 + symbol1 + alpha2 + alpha1 + symbol3 + num2 + alpha4 + symbol2 + alpha4 + alpha3 + alpha1 + symbol2 + num1
        return random_password
    else:
        return "::: sorry invalid selection ::: "

type_of_pass = input('''|| Enter 1 or hard for hard password ||
|| Enter 2 or medium or intermidate for medium password||
|| Enter 3 or easy or normal for normal password ||
:::--> ''')

print("\n",'your unique pwd: ', random_password(type_of_pass))
print("\n::: by Ishtiuk Ahammed :::\n")
