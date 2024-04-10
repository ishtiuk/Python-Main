#
#          Swap Minimum

# In selection sort you select the minimum element and then bring it to the left.


#   Let's explain more......

# Main Concept:

# 1. For each position, loop elements on the right.
# 2. Find the minimum numbers on the right.
# 3. Swap these two elements (Bring the 'min element' to the current position and send the 'current element' to the 'min element' position)
# 4. Repeat steps from 1 to 3.



# let's do it from step by step.

# first of all, we need to find the 'minimum number's index' from the List.
# so, let's run a 'for' loop through the List         (it'll be the inner 'for' loop)


#  |||  this inner 'for' loop will continuously search for the minimum element and bring the 'minimum' element to the left side...... 😎 |||


# arr = [99, 54, 45, 23, 21, 13]

# mini = 0

# for j in range(len(arr)):
#     if arr[j] > arr[mini]:
#         mini = j





# so, let's put the first 'inner for loop' in the outer 'for loop', 

arry = [99, 54, 45, 23, 21, 13]

for i in range(len(arry)):                            # for each rotation of 'outsider for' loop the 'inner for' loop will find the 'minimum element's index' and bring that 
                                                      # to the first, sequentially.....
    mini = i

    for j in range(i + 1, len(arry)):               # the inner 'for' loop will start from 'i + 1' index, 
        if arry[mini] > arry[j]:                    # that's why it should not check the first element and previous 'minimum elements'
            mini = j
    print('Just for monitoring:',arry)
    temp = arry[i]
    arry[i] = arry[mini]
    arry[mini] = temp

print()
print(arry)

# a = 5
# b = 4

# temp = a
# a = b
# b = temp

# print(a, b)