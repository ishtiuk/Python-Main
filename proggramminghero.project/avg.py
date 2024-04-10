len = int(input("How many numbers do you want to enter: "))
numbers = []

for i in range(len):
    number = int(input("Enter number: "))
    numbers.append(number)

total = sum(numbers)
avg = total / len
print(avg)