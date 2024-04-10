# 
#  "Set" is also a cousin of "list".

# but "Set" is mutable but not sequential and unique values container.

# Set is a not sequetial so, get data from Set isn't possible by index. But '.pop()' function also works here too.

a = set()     # emply set creation method. 

a = {8, 6.1, 'dfdf', 8, 4, (5, "fdf", 5), True}


#    |||||||||||||||   Adding DATA to SET       ||||||||||
#  Python provides the 'add' function to add element to SET ........ :-D"""

a.add("C++")         # adding method to a SET
print(a)

# ||||||||||||||||      Removing DATA or element from SET      ||||||||||||

# removing Data is interesting 😁

# there are two methods to remove element from set. 
# 1. use function "remove()"
# 2. use function "discard()"

# if we want to remove an Element which doesn't exist in the SET, then "my_set.discard()" will not through any Error, 
# but the "my_set.remove()" will through Error if the Element doesn't exist on the SET....

a.remove("dfdf")
print(a)

a.discard("ydfdfj")
print(a)



# overall, Set provides us the unique values, that means Set doesn't shows duplicated values or twice time. 😏

# and one more thing, set supports also types of data types except Set and List and Dictionary . 😒




#   |||||||||||||||||           Maths with SET         |||||||||||||||

# Do you remember the school life maths, we have learnt about SET in mathmatics .

#        ||||||||||||||    UNION    |||||||||||||||||
# there were Union in SET which contains the all values of the values of both sets common and not common values.

# so, we can perform the UNION task between sets by two methods:
# 1. Using the '|' Pipe Operator (python Operators: -, +, *, /, //, % etc)
# 2. Using "union()" method. 

b = {2, 4, 9, 3}
c = {7, 8, 9, 2}

print(b.union(c))

print(b | c)


#        ||||||||    INTERSECTION    |||||||
# There INTERSECTION in SET which contains only the common values between sets....

# so, we can perform the UNION task between sets by two methods:
# 1. Using the '&' Pipe Operator (python Operators: -, +, *, /, //, % etc)
# 2. Using "intersection()" method. 

print(b.intersection(c))

print(b & c)


#      ||||||||||   DIFFERENCE    ||||||||||
# There DIFFERENCE in SET which contains difference of Sets......

# so, we can perform the DIFFERENCE task between sets by two methods:
# 1. Using the '-' Minus Operator (python Operators: -, +, *, /, //, % etc)
# 2. Using "difference()" method. 

print(b.difference(c))

print(b - c)



##
#