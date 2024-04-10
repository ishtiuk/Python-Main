len = int(input("Enter how many numbers do you want to enter: "))
total = 0

for i in range(len):
    number = int(input("Enter number: "))
    total = total + number

avg = total / len
print(avg)

#this is the same program given below using while loop, the two program will do same thing. but I think using 'for' loop is better, cause it saves some line. Like as, if I use 'while' loop,I have to declare 'i' and increase i inside loop "i += 1"
'''len = int(input("Enter how many numbers do you want to enter: "))
total = 0
i = 1

while i <= len:
    number = int(input("Enter number: "))
    total = total + number
    i += 1

avg = total / len
print(avg)'''
