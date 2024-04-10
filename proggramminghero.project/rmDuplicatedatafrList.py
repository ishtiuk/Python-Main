def remove_duplicate(items):
    unique_list = []
    for item in items:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
lottery_numbers =  [22,11,3,1,4,5,5,2,2,11,66,89]                   


# __________________________________________________________________________
# it is the another alternative way to print the unique element

a = [1,2,2,3,4,5,6,6,88,87,88]                                                                           
print(a)
a = list(set(a))
print(a)
# ____________________________________________________________________________



# this can be used to add 1 number in lottery_numbers list
# x = input()
# y = int(x)
# lottery_numbers.append(y)

x = remove_duplicate(lottery_numbers)
print(x)
# print(lottery_numbers)
