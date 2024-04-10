
# 

# Complete Pseudocode for Binary Search

# function binary_search (list, serching_value):
#     low = 0
#     high = length of the list

#     while low <= high:
#         mid element = average of low and high
#         if mid element < serching_value:
#             Element will be on the right side
#             low = mid

#         elif mid element > serching_value:
#             Element will be on the left side
#             high = mid 

#         else:
#             You got the element
#             return the mid


# binary Search Algorithm

# the Word Binary means Two, so.......

# it called the Binary Search Algorithm. Because this Divides the Search Aera into Two Parts

  
# aaaaandd one more thing , Binary Search Algorithm follows the "Divide and Conquer Approach"


# this Algorithm Divides the Searching Area Gradually and at last, Conquers the Result.... 😎😎




def binary_search(search, lst):
    low = 0
    high = len(lst)
    search = search

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == search:
            print('index: ', mid)
            break

        elif lst[mid] < search:
            low = mid

        elif lst[mid] > search:
            high = mid


lst = [3, 4, 10, 53, 64, 69, 90, 533]
lst.sort()
search = 90
print("Printing list for surveillance: ", lst)

if search not in lst:
    print("{} not found!".format(search))
else:   
    binary_search(search, lst=lst)


#  but here are a Condition that Binary Search Algorithm only works on Sorted List 😏🥴,
# so we have to convert a 'list or Array' into A 'ascending array' before running the 'Binary Search Algorithm' on it.