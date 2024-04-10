def odd_number_square(len):
    square_list = []
    for i in range(len+1):
        if i%2 == 0:    
            square = i ** 2
            square_list.append(square)
    return square_list
number = int(input("Enter number range: "))
print(odd_number_square(number))