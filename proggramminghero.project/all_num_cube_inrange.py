def all_num_cube_inrange(range_num):
    sum = 0
    for n in range(range_num+1):
        sum += n ** 3
    
    return sum

print("Sum of all numbers:", all_num_cube_inrange(int(input("Enter number range: "))))
