
#  To measuring Time Complexity... you need Two thing:

# 1. Input Size = n
# 2. Growth Rate = O


# here are a 'Nested for Loop' below....


cls_one = ['Jeremy', 'Waller', 'Zion', 'Cervantes', 'Tabitha']
cls_two = ['Roach', 'Heaven', 'Henry', 'Neveah', 'Bowers']
cls_three = ['Ashlynn', 'Choi', 'Brooke', 'Hardy', 'Valentino']

school = [cls_one, cls_two, cls_three]

search = 'Roach'
                                                        # here, Input is 'school' and let's say Growth Rate 'O' is Constant = 1 second..
                                                        
for clss in school:                                     # for Each student outer 'for' loop is going to the every Class 
    for student in clss:                                # then, the 2nd inner 'for' loop is going to the every Students or Elements
        if student == search:                           # that means time for 1 Class we are going to 'n' number of students in the Inner 'for' Loop
            print("Student found.!", student)           
                                                        # now this Multiplication will be:
                                                        
                                                        # For 1 class, you run 'n' students
                                                        # For 2 class, you run '2 * n' students
                                                        # For 3 class, you run '3 * n' students
                                                        # For 'n' class, you run 'n * n' students


                                                        # Now, n X n could be written as '𝑛2', Right? 


# So, the Time Complexity of a 'nested Loop is':  O(𝑛2)


# it's read as 'ooh an square' 😎