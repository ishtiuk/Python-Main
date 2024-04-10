#

# we can get all the Keys from a Dictionary Data Structure using a special function or method 😎, let's see...
# we can enlist those 'keys' using the 'list()' method 😏


dicts = {'mango': 500, 'lichi': 366,'pineapple': 422, 'banana': 155}

fruits = dicts.keys()
lst_of_keys = list(fruits)

print(fruits) 
print(lst_of_keys)

print(type(fruits))    # let's see type of this 😉



# and we can also get all the Values from a Dictionary Data Sturcture using another special function or method 😎, Let's also see that...
# we can enlist those 'values' using the 'list()' method 😏

dicts = {'mango': 500, 'lichi': 366,'pineapple': 422, 'banana': 155}

prices = dicts.values()
lst_of_values = list(fruits)

print(prices) 
print(lst_of_values)

print(type(prices))    # let's see type of this 😉





# ============ Looping Dictionary Keys ============= 😉

print()

for key in dicts.keys():
    value = dicts[key]
    print(key+"'s price is:", value)



#                   interesting 😎😎 