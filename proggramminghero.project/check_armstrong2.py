def check_armstrong2(num):
    temp = num
    leng = len(str(num))
    sum = 0
    

    while temp > 0:
        last_digit = temp % 10
        sum += last_digit ** leng
        temp //= 10                             # temp //= 10 is alternative of temp = temp // 10

    
    return sum == num 
    
number = int(input("Enter number to check armstrong: "))

if check_armstrong2(number) is True:                                          
    print("The number is armstrong")                  # alternative or short form of this=  if num == sum:
elif check_armstrong2(number) is False:                                                 #                                           result = True
    print("The number is not armstrong")                                            
                                                      #                                     else:
                                                      #                                           result = False
                                                      #                                     return result '''
                                                                                


