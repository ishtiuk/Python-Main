#
#
# The Bubble Sort is the simplest Sorting Algorithm. The main concept is:

# 1. Compare two adjacent elements
# 2. If the first item is Bigger than the second item then swap it.
# 3. Run the loop for n-1 items.
# 4. Keep doing it for all the elements.


# let's try.....



a = 5
b = 2                                           # remember, a simple 'swaping' system is needed before makin Bubble_sort And Selection_Sort Algorithm.
print(a, b)                                     # it'll make your task easier, Trust me it'll be very helpful 😎😎

tem = a
a = b
b = tem
print(a, b)
print()



# length = len(array)

array = [23, 2, 99, 45, 66]

# inner 'for' loop, it will continuously Compare two adjacent Elements and swap them ....

# for i in range(len(array) - 1):
#     if array[i] > array[i + 1]:
#         temp = array[i]
#         array[i] = array[i + 1]
#         array[i + 1] = temp

print(array, '\n') 


# now, time to loop for each single 'elements', so, let's dump the 'first or inner 'for' loop' into a outter 'for' loop ,
# the outter for loop will loop the inner for loop for each element and finally we'll get the 'sorted list'


for j in range(len(array)):
    
    
    for i in range(len(array) - 1):
        print('Monitoring:', array)
        if array[i] > array[i + 1]:
            temporay = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temporay

print('\n', array)



# aaaaaaaannnnnnnnnnnnnnnndd that's all, we got the sorted list........ 😎