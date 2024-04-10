phbkdb = ['01815632823', '01860781599', '01819825147' ]

number = input()
#the number which started with 0 they are not allowed as a int but they are allowed as float number in list or array. in that case I have to declaire them in list or array as string.

for dbcheak in phbkdb:
    print('fresh fruit ' + dbcheak)
    #this line is added from Proggramming Hero app learnings. 
    
    if number == dbcheak:
        print("  ")
        print("found. this number exist in database : ☢ ",number," ☢")
        print("  ")
        break
    else:
        print("  ")
        print("Alert..!! number not found. this number is stored to Database..!!")
        phbkdb.append(number)
        print("  ") 
        print(phbkdb)   
        break