#
#  To measure the 'Time Complexity', will need 2 things  . 😎

# 1. The Input Size.   =  'n'
# 2. The growth Rate   =  'O'

# if you have to Search any element from any List, you will obiously run a For loop 
# and check the first Element and will keep going all the Way towards the last Element, Right...?? 


# now Check Check and Check 🥴🥴 

# If the List has 10 Elements, you have to check 10 times
# If the List has 20 Elements, then you have to check 20 times
# And if the List has 1000 Elements, then you have to check 1000 times 🥴 

# Or simply if the Array or List has 'n' number of Elements, you have to Check 'n' times... 🥴🥴


#  === Linear ===
# Now, if you increase one Element in the List, you have to check one more Element, Right?
# Thus, if you increase or add 10 more Elements then you have to check 10 more Elements... 🙂🙂


schl = ['Jeremy', 'Waller', 'Zion', 'Cervantes', 'Tabitha', 'Roach', 'Heaven', 'Henry']
find = 'Roach'

for i in schl:
    if i == find:                                  #   here time complexity = O * n = O(n)
        print(schl.index(i), i)
                                                    # imagine the growth rate 'O' is constant that's  1 second, that means to check 1 element it takes 1 second time
                                                    
                                                    # so for input size = 'n' = here '8' , it will take   ' 1 * 8 = 8 ' seconds, right?