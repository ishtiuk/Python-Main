def second_largest(anything_lsit):

    anything_lsit.sort(reverse = True)                       
    second_largest = anything_lsit[1]

    return second_largest

nums = [78,2,98,64,5,32]
print(second_largest(nums))
    