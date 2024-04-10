
#  'Tuple' is a way to store data like list, but it starts with 1st paranthesis and it's Immutable. But List is mutable and List also a Data Structure.

#|||||||||||||||  Remember that, Tuple execution time is lesser that List execution, so if you have to use a Immutable data then use Tuple instead of List. 
That could make your program or software little bit faster...!! :D (Because in coding 1 nano sec also matters) ||||||||||

tup = (5, 6, 4, 65, 4, 66)

print(tup.index(65))
print(tup[0])

# but we can't change Tuple's values

# tup[5] = 988          # but we can't change Tuple's values
# print(tup)


# now, let's talk about 'Set' |||||||||||

# set basically store one value just once, let's see. It starts with second paranthesis...

s = {55, 44, 55, 64, 45, 65, 64}
print(s)         # as we can see it has stored and returned one value just once, that means 'Set' doesn't contains any duplicate  :-D  ||||





# now, |||||||||||||  Tuple Vs Set Vs List ||||||||||

# 1. Tuple stores values but they are unchangeable or immutable. So, it doens't follow the rules of Data Structure. (Tuple can store more than one data, special structure to store data (,), 
# but Tuple can't change data, so it has no specific way to add or remove data, That's why 'Tuple' isn't a Data Structure )

# 2. On the other hand, 'Set' doesn't follow sequence to store data, it stores data is random sequence. As it has no sequence so data can't access from 'Set', Right? So, it's also not a Data Structure.
