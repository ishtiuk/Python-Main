def decimal_to_binary(num):
    if num >= 1:
        decimal_to_binary(num // 2)
        print(num % 2, end='')

number = int(input("Enter your decimal number to covert in binary: "))
decimal_to_binary(number)
print("  ------- this is the binary of", number)                                                                # but I recommand the another method to convert in binary..........


