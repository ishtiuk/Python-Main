def interest_calc(principal, rate, time):
# Interest = ?

    interest = (principal * time) * (rate / 100)                                            

# print("Interest : ", interest)                                              # here, I used the formula which, I have learnt in class 5. Formula is : I = Pnr ,
    return interest                                                                        # here '%' sign cannot be used as the sign of 'percentage'here, because '%' sign is considered in Python to get remainder.
                                                                            # so, I used (rate / 100) instead of percentage.

principal = int(input("Enter Principal: "))
rt = float(input("Enter Rate: "))
time = float(input("Enter Time: "))

print(interest_calc(principal, rt, time))

