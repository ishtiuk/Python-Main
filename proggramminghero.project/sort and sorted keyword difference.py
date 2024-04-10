# for the case of 'sort' keyword:
num_list = [5,8,2,5,9,8,454,45,67]
num_list.sort()
print(num_list)                            # here,'sort' keyword can arrange the numbers from small to large, or large to small. now,
                                           # I'm telling how can be it possible, If we write "listname.sort()", then generally it will arrange the numbers form small to large as default,
                                           # but when we will write, "listname.sort(revers=True)" or "listname.sort(reverse=1)",it will arrange the numbers from large to small,
                                           # because we have reversed it by telling 'reverse=True'
                                           # on the other hand, if we write, "listname.sort(reverse=False)" or "listname.sort(reverse=0)",  it will arrange the numbers from small to large again,
                                           # but I think this is meanless, because, if we use "listname.sort()" it will arrange form small to large automatically, so "listname.sort(reverse=False)"
                                           # writting, which will do the same thing, it is meanless

nums = num_list.sort(reverse=True)         # one disadvantage of the 'sort' keyword is, this cannot be override, wait, I'm clearing this, we have written,'num_list' now we cannot include                           
print(nums)                                # elements of this list by writting 'nums = num_list.sort(reverse=True)' this cannot be succeed, this will return 'None' as output.


# for the case of 'sorted' keyword:
sum_list = [8,7,9,1,2,3,3,5,5,7,5,64,87,766]
sumlist = sorted(sum_list)                 # but on the other hand, we can override the list, such as, if we declare a list named 'sum_list', then we can write 'sumlist = sorted(sum_list)' or 
print(sum_list)                            # we can override the list with same name, by writting 'sum_list = sorted(sum_list)' 
print('''


''')                                           # but one disadvantage of the 'sorted' keyword is, we cannot reverse it like the 'sort' keyword.

def second_largest(num_list):
    num = sorted(num_list)
    second_largest_1 = num[-2]

    num_list.sort(reverse=True)
    second_largest_2 = num_list[1]

    return second_largest_1, second_largest_2              # and at last, these both two keywords, 'sort' and 'sorted' are usable in Function too.... 

num = [4,5,2,3,7,8,9,4,5,68,78]
print(second_largest(num))