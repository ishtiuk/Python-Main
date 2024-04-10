#
#                   Defination of 'Recursion'

# If a function calls itself, it is called a 'Recursive Function'. It's called recursive because it recursively calls itself....


#      usage of Recursion  >>

# 'Recursion' could make a Complex problem Simple. 😎 But yeah, if you try to force recursion in a simple situation, your code might become more Complex 🥴🥴
# so, use 'Recursion' or recursive function some carefully....



# characteristics of 'Recursive Function'..:: --
# 1. A stopping condition or base condition
# 2. Call the function itself.


# that means a Recursive Function should have a Stopping Condtiion, Otherwise the Recursive will not have no limit, Right? 
# so, a sTopping condition is must needed..

# and the main function, which will be called untill True the Stopping Condition

# Example Factorial Function 1

def factorial(num):         

    if num <= 0:            # << (Stopping Condition) 😃
        return 1

    return num * factorial(num - 1)      # calling the 'Function' by itself 🙂


print(factorial(5))



# Factorial using Loop: 
def fac(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print(fac(4))



# more Recursive Functions.....

def binary_recursion(num):
    if num >= 1:
        binary_recursion(num // 2)
        print(num % 2, end='')
        
    
binary_recursion(10)
print('\n')

def reverse_sentence(sentc):

    if len(sentc) == 0:
        return sentc
    return reverse_sentence(sentc[1:]) + sentc[0]

print(reverse_sentence(input('Enter word: ')))