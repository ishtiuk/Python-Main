len = int(input("Enter how many numbers do you want to enter: "))
i = 1
numbers = []

while i <= len:
    number = float(input("Enter number: "))
    numbers.append(number)
    i += 1
    
total = sum(numbers)
avg = total / len
print(avg)



