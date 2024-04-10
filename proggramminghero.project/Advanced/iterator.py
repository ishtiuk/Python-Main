
# Iterator is simply a Object which is iterable through loops...
# 
# such as List, strings, tuples and more data classes. 
# 
#   ||||||||||||||   Iterators ||||||||||||||\
# 'Iterator' is an Object which can be iterated upon which will return data, one element at a time. 
# 'Strings, Lists, Tuples and more from which we can create the iterators objects..
# 
# 
# Iterator Class should must have two special Methods, They are :    "__iter__()"   and the  "__next__()" 

# A python iterator Object must implement two special methods, "__iter__()" and "__next__()", collectively called the iterator protocol....


#   now iteresting thing......

# the __next__() method returns the next one element...

# now.................. when we use an for loop to traverse any iterable Object, then internally behind the scene it uses the 'iter()' Method to make those Object 
# like: Sting, list, tuple, set to make them iterable, then uses the 'next()' or '__next__()' method to loop over or get the next element continuously.

# aaaaandd, when we reach the end and there is no more data to be returned, then it will raise the "StopIteration" named Exeption. And thus 'for' loop stops the itering...
# ahh, so we have learnt about the core part of itering and loops 😎,  interesting................ 🤩🤩

try:
    a = 'dfd'
    a = iter(a)
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
except StopIteration as stop:
    print(stop)
    print('stopped')

a = {5, 6}
# a = iter(a)
# print(a.__next__())
# print(a.__next__())
