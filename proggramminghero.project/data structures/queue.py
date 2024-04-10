# 'queue' is a kind of list.

# One important feature of a 'queue' is "FIFO" method, full meaning 'First In First Out', that means a 'queue' returns at first that data which has added at first.
# If any list does not follow this "FIFO" method, then that List will not be considerd as 'Queue'.

# Example 1:
# now, imagine about a waiting line in a bank, or bus counter and whatever. What you can see there? There that people can get first service who came first there, like if anyone stands first then, he will get the ticket at first. 


# so, here are following the "FIFO" method.


# to take the first element or value from a 'queue', you have to use 'pop()', but hey wait a sec, man. 
# you can't use pop() here like the stack method, because generally, by default, the keyword, 'pop()' takes the last element from a List,
# untill you pass a Index number, there like, "pop(4)", here it will take the element from a List which is located in the 4 Index.

# let's see an example, 


achars = ['a', 'b', 'c', 'd', 'e', 'f']
four_indexed =achars.pop(4)

print(four_indexed)

# so, if we want to follow "FIFO" method for a 'Queue', then we have to take the first element first. Right________??
# that's very simple, we have to take the Indexed number 0 everytime, like: 'varrible.pop(0)', here, it will take the first element.
# like: 

for i in range(len(achars)):
    first_element = achars.pop(0)
    print(first_element)

# so, now as we can see it is taking the first element everytime.
# so, it's following the "FIFO" method, that means it's a "Queue" typed data structure....________!!!!!!!!!!!