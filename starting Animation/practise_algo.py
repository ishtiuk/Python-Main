# binary search algo.......

lst = [5, 6, 7, 8]

search = 8

l = 0
u = len(lst)

while l <= u:
    mid = (l + u) // 2

    if lst[mid] == search:
        print(f"found: {mid}")
        break
    
    if lst[mid] < search:
        l = mid

    elif lst[mid] > search:
        u = mid

# is_prime?
    
# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(29))


# bubble sorting....

lst = [7, 5, 4, 3]

for j in range(len(lst)):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            temp = lst[i]
            lst[i] = lst[i + 1]
            lst[i + 1] = temp

# print(lst)



lst = [7, 5, 1, 4, 3, 2]

for i in range(len(lst)):

    mini = i

    for j in range(i+1, len(lst)):
        if lst[mini] > lst[j]:
            mini = j

    temp = lst[mini]
    lst[mini] = lst[i]
    lst[i] = temp

print(lst)