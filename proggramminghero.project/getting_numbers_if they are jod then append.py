len = int(input("How many numbers you want to enter?: "))
numbers = []
i = 1

while i <= len:
    number = int(input())
    if number%2 == 0:
        numbers.append(number)
    i += 1
total = sum(numbers)
print(total/len)
print("Here are the even numbers in a list:", numbers)