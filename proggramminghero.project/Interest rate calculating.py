def interest_rate(principal, interest, time):
# Interest rate = ?

    rate = (interest / (principal * time)) * 100                                                          # I = Pnr , 

    return rate

principal = int(input("Enter Principal Amount: "))
interest = float(input("Enter Interest Amount: "))
time = float(input("Enter Time: "))

print(interest_rate(principal, interest, time))
