import time

def binary_converter(number):
    bits = []
    binary = ''
    while number > 0:
        bits.append(number%2)
        number = number // 2

    bits.reverse()

    for bit in bits:
        binary += str(bit)

    return binary

        # for bit in bits:

print('\n')
bit = binary_converter(int(input("Enter number to convert in binary: ")))
print('\n')
print('converting to binary... ')
time.sleep(1)
print('\n')
print("Binary: ", bit, '                                        ::: Powerd by HxD Corpo :::')
print('\n')