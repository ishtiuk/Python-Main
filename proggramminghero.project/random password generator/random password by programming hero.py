from math import perm
import string
import random


def random_pwd_generator(size):
    password = ''
    all_chars = string.ascii_letters + string.digits + string.punctuation
    for i in range(size):  
        char_pwd = random.choice(all_chars)
        password += char_pwd
    
    print(password)

random_pwd_generator(int(input("::: How many character do you want? ::: ")))