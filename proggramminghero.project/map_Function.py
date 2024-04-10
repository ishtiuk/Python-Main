
# Map function is a Function which applies a Function for a Whole List....

# like below......

lst = [2, '5', '35', 7, '9', '5']

# lst = map(int, lst)
# print(lst)

# for i in lst:
#     print(type(i), i)


lst = list(map(int, lst))       
print(lst)

# Map function takes two argument, 1st argument will be the specific 'function' which we want to apply on the List, 2nd argument will be the List. :)



# another Example

def pow(n):
    return n ** n

arrr = [6, 4, 7, 4, 6]
arrr = list(map(pow, arrr))

print(arrr)