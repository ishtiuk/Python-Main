# 
#  |||||||||||||||    Tuple   ||||||||||||||

# "Tuple" is a cousin of our favorite Data Structure "List" 😁. Because it almost similar to List. But we can't huge types of operation with "Tuple" as our "list" 😒

# Now, the main difference between TUPLE and List is. LIst is mutable or changeble but Tuple is immutable that means unchangeble. 

# If Tuple is defined once then it can't be changed.... 🙄. but we can use almost al other operations and functions which we can use with List. 

# like: sum(), tuple.count(), tuple.index(element_nm), tuple[0], etc............
# but can't use the functions like: remove(), pop() , because it's immutable Data Type

# and one more thing, Tuple is sequential, so we can fetch or use data from Tuple by index......

my_tuple = (6, 6, "fddf", [65, 444, 'hello_nc', 66.55], 66.5, 9595)

# print(sum(my_tuple))
print(my_tuple.count(6))
print(my_tuple.index('fddf'))

print(my_tuple[4])



#        nowwwwwww............... Tuple is immutable Data Type. It's only  Give the   "Read" access not "Write" access.
# on the other hand, List gives us the all REad write access. That's way List is a DATA Structure. But not Tuple. 




# Now, question? Why we will use Tuple. 
# let's say you have some datas which don't need to be changed. 

# like a Result of every sub of 1st semester , or the ratings of your product. This infos don't need to be changed, Right? 

result_tuple = (80, 70, 90, 60, 80)
print(result_tuple)

ratings = (4.5, 6, 3.4)
print(ratings)


# ||||||   annnnnnnnddd, the execution time of a Tuple is less than  a List. So, it may make your code or program faster. :D........ ||||
# so, if you have specific datas for your program which don't need   |||||||||
# to be changed than store them in a "Tuple", instead of a "List".  ||||||||


# 