def calculator(num1, symbol, num2):

    if symbol == '+':
        print("\nsum = ", num1 + num2)

    elif symbol == '-':
        print("\nsubstraction = ", num1 - num2)
    
    elif symbol ==  '*':
        print("\nmultiplication = ", num1 * num2)
    
    elif symbol ==  '/':
        print("\ndivition = ", num1 / num2)

    return "\npowerd by HxD\n"

number1 = float(input("\nEnter the first number: "))
symbol = input("Enter symbol: ")
number2 = float(input("Enter the second number: "))

print(calculator(number1, symbol, number2))