pd = '1139'
pwdinp = input("Applock Password: ")

if pwdinp == pd:
    print("Welcome, authentication passed.")
else:
    print("Password is incorrect.!")
    print("Do you want to reset password?")

    in_pch = input()
    
    if in_pch == 'yes':
        print("ok, proccessing: ")
        pd = input()
        print(pd) 
    else:
        print("ok, go away")



# I want to run this again. But now, I have no knowledge about it. So, I'm lefting it now, but soon I will develop the applocker proggram Inshallah.

