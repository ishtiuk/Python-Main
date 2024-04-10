def calculator(num1, sym, num2):
    if sym == '+':
        sum = num1 + num2
        return sum
    elif sym == '-':
        substraction = num1 - num2
        return substraction
    elif sym == '*':
        multiply = num1 * num2
        return multiply
    elif sym == '/':
        division = num1 / num2
        return division

number1 = float(input("Enter first number: "))
symbol = input("What you want to do: (+, -, *, / ::: ")
number2 = float(input("Enter second number: "))

print(number1,symbol,number2,'=',calculator(number1, symbol, number2))