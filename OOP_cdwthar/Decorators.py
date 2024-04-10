
#                         |||  defination of Decorators  |||

# A 'decorator' is a function that takes another function as its argument, 
# and can return yet another function 

# def function1():
#     print('Hey, Sir')          

# func2 = function1              # here, function1 was stored in 'func2',
#                                # so, even you delete the 'function1', by typing del 'function1'
# del function1                  # still 'func2' to will return function1' s values, 
#                               # because 'funtion1's value was stored in 'func1' function
# func2()


def funcreturn(num):
    if num == 0:            # so, now we have proved that a 'function' can return or able to return another 'function' (N.B: 'print' and 'sum' both are built in function in Python)
        return print
    if num == 1:            
        return sum          # here noitce that, 'print' and 'sum' both are built in function in Python

a = funcreturn(1)
print(a)

b = funcreturn(0)
print(b)


# we can give 'function' in another 'function' and can return a 'function' with a help of another 'function'.


def decora1(func):
    def nowexec():
        print("Executing")
        func()
        print('Executed')

    return nowexec 
    # return func

@decora1                    # this is '@' decorator which does the same thing as 'whoishxd = decora1(whoishxd)' decorator.
def whoishxd():
    print('hello')

whoishxd = decora1(whoishxd)     # it's the 'decorator'..!! because it is passing a function which is 'whoishxd()' as aa aurgument' of 'decora1()' function.          || # notice that, 'whoishxd' is a simple varible, but it holds the value of 'decora1()',
                                                                                                                                                                    # || so, it became a function too, because it (whoishxd varrible) stores the 'decora1' function
# print(type(whoishx))
print(decora1)                  # it prints the 'decora1' function's memory location


whoishxd()                   # as, we passed 'whoishxd()' 

# |||  defination of Decorators  |||

# A 'decorator' is a function that takes another function as its argument, 
# and can return yet another function 