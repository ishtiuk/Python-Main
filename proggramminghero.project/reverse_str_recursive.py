def reverse_string_recursive(sentence):
    # while True:                               # here "while" is not needed, becasue we are doing the same thing as while loop 
                                                # on the " else:
                                                #             return reverse_string_recursive(sentence[1:]) + sentence[0]      
                                                # we are doing this again and again until the "if" becomes true, that means we are looping this manullay
                                                # so, obiously "while" loop isn't needed here. 
    if len(sentence) == 0:
        return sentence
    
    else:
        print(len(sentence))
        return reverse_string_recursive(sentence[1:]) + sentence[0]
        

inp = input("Enter your sentence to reverse: ")
inp_entering = reverse_string_recursive(inp)
print("Reversed string is: ", inp_entering)






































