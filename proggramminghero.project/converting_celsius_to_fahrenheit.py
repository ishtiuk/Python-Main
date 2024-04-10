def celsius_to_fahrenheit(celsius):

    fahrenheit = (celsius*9)/5+32

    return fahrenheit

fahrenheit_receving_unit = float(input("Enter temperature in celsius: "))
print(celsius_to_fahrenheit(fahrenheit_receving_unit))
