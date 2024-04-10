#
# =============   Stack ============

# When you use the 'Last in First Out (LIFO)' policy the data structure is a Stack. You could use a 'List' or a 'Linked List' or any other suitable data
# structure to implement this policy. 



# ============   Queue =================

# Similarly, when you enforce or use the rule of 'First In and First Out (FIFO)' policy, the data structure becomes a queue... 




# that means any kind of Data Structure can be a Queue or Stack if that follows the (LIFO)  or (FIFO). If that follows "LIFO"  that's
# a STACK and if that follows 'FIFO' then that's a QUEUE... 




#  =========  Enqueue and Dequeue ==============

# Two side things. The process of adding an element to a 'queue' is called 'Enqueue'. The process of removing an element from a 'queue' is called 'Dequeue'. 




#   =====   Now, question? Why most of the times List is used to implement a Stack or Queue? 🤔 ===== 

# Most of the time List is used to implement a Stack or Queue. Because, List is the most important and widely used data structure. 


quz = input('''Which one is used to create a Stack or a Queue?
A. Arm and Hammer
B. Bricks and Paints
C. List
:-->> ''').upper()

if quz == 'C':
    print('Correct answer, Sir')
else:
    print('Wrong answer, Sir')
