# 'stack' is a kind of list.

# One important feature of a stack is "LIFO" method, full meaning 'Last In Fist Out' , that means a stack returns at first that data which has added at last.
# If any List does not follow this "LIFO" method, then that List will not be considerd as a "Stack".

# Exmple 1:
# now, imagine that you are collecting plates after dinner from table. So, what you will do? 
# You will collect the first plate and then second plate, and will place the second plate on the first plate. And one by one you will collect the all plates. Right?
# imagine there were 5 plates. So, the first plate is at the bottom, Then if you go to wasth them. then what will you do now?

# you will take the last or 5th plate at first, that means you are following 'LIFO' method, so, the plates are a 'Stack'

# Example 2:
# now, imagine once more, what you wears in winter? firstly, a gengi then a shirt then a suater and then a jacket. Right?
# now, what you will do to take off those clothes? firstly you will take off the Jacket then Suater then Shirt then Gengi, so what happened? You have also followed the "LIFO" rule here.
# so, here your winter clothes are also a "Stack"



# to take the last element or value from a "stack", you have to use 'pop()' keyword. which gathers the last element at first and maintains the "LIFO". Like below:-

chars = ['a', 'b', 'c', 'd', 'e']
last_element = chars.pop()                              # here it has gathered the last element
print(last_element)                                     


cha1 = chars.pop()
cha2 = chars.pop()                                      # you can store these values in different varribles too.
cha3 = chars.pop()
cha4 = chars.pop()

print(cha1, cha2, cha3, cha4)