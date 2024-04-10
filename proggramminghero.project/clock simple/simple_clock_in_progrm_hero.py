import time

hour = int(input("Enter current hour: "))
minute = int(input("Enter current minute: "))
second = int(input("Enter current second: "))
print('override: ', hour, minute, second)
def display():
    print(hour,":",minute,":",second)


def clock():
    global hour
    global minute
    global second
        
    second += 1
    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 24:
        hour = 0

    print('\n')


while True:
    clock()
    display()
    time.sleep(1)