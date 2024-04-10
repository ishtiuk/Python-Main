import random
import string

def gmail_usrnm_pwd_provider(firstnm, lastnm, pwdlen):

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(pwdlen):
        chars = random.choice(all_chars)
        password += chars


    gmail_name = firstnm + '.' + lastnm + '@gmail.com'


    print('your username :: '+ gmail_name,)
    print("password :: "+ password)

firstname = input("Enter your first name: ")
last_name = input("Enter your last name: ")
size = int(input("How long password do you want? :: "))

creditals_transfer = gmail_usrnm_pwd_provider(firstname, last_name, size)
