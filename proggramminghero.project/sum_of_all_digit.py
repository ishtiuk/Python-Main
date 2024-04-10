def sum_of_all_digit(num):
    sum = 0
    while num > 0:
        last_num =  num % 10
        sum = sum + last_num
        num = num // 10
    return sum
digit = int(input("enter number: "))
print(sum_of_all_digit(digit))