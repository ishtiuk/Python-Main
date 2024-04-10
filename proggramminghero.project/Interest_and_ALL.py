def all_amount(principal, rate, time):

    all = principal * ((1 + (rate / 100)) ** time)
    
    return all

principal = int(input("Enter Principal Amount: "))
rate = float(input("Enter Interest Rate: "))
time = float(input("Enter Time duration: "))

print(all_amount(principal, rate, time))