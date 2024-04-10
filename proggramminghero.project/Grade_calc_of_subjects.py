def grade_calc():
    num_list = []
    subs_length = int(input("\nEnter amount of Subject: "))
    print('\n')
    for i in range(subs_length):
        sub_num = float(input("Enter occupied number: "))
        num_list.append(sub_num)

    averege = sum(num_list) / subs_length

    if averege > 90:
        print("\nYour Grade is: A")
    elif averege > 80:
        print("\nYour Grade is: B")
    elif averege > 70:
        print("\nYour Grade is: C")
    elif averege > 60:
        print("\nYour Grade is: D")
    else:
        print("\nYour Grade is: F. Better Luck next time.")

grade_calc()
print("\nGrade calc Powered by HxD Corpo\n")
