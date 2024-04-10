print('\n')
print("Temperature Conversion Program by HxD")
print('\n')
print("Selections:::\n::: Press 1 to Enter Celsius ::: \n::: Press 2 to Enter Fahrenheit ::: \n::: Press 3 to Enter Kelvin ::: ")

choice = int(input("    Enter your selection: "))

if choice == 1:
    temp_celsius = float(input("    Enter temperature in Celsius Unit: "))
    fahrenheit = round((((temp_celsius * 9) / 5) + 32), 2)
    kelvin = temp_celsius + 273.15
    print("Temperature in Fahrenheit: ", fahrenheit)
    print("Temperature in Kelvin: ", kelvin)

elif choice == 2:
    temp_fahrenheit = float(input("Enter temperature in Fahrenheit Unit: "))
    celsius = round((5 / 9) * (temp_fahrenheit - 32), 2)
    kelvin =  round(((5 / 9) * (temp_fahrenheit - 32) + 273.15), 2)
    print("Temperature in Celsius: ", celsius)
    print("Temperatuer in Kelvin: ", kelvin)

elif choice == 3:
    temp_kelvin = float(input("Enter temperature in Kelvin: "))
    celsius = temp_kelvin - 273.15
    fahrenheit = round((((9 * (temp_kelvin - 273.15)) / 5) + 32), 2)
    print("Temperature in Celsius: ", celsius)
    print("Temperature in Fahrenheit: ", fahrenheit)

else:
    print("Sorry..!! Invalid Selection.!")
