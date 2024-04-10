import time

print("::: Digital Clock made by HxD Corpo :::")

hour = int(input("Enter the current hour: "))
minute = int(input("Enter the current minute: "))
second = int(input("Enter the current second: "))


while True:

    second += 1

    if second >= 60:
        minute += 1
        second = 0

    if minute >= 60:
        hour += 1
        minute = 0

    if hour >= 24:
        hour = 0

    print(hour,':',minute,':',second)
    time.sleep(1)

    



