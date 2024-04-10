def all_num_square(len):
    square_list = []
    for i in range(len+1):
        square = i ** 2
        square_list.append(square)
    return square_list

number_range = int(input("Enter number range: "))
print(all_num_square(number_range))