#

#   Classification of Linked List:

#   1. Singly Linked List
#   2. Doubly Linked List
#   3. Circular Linked List


# ===========   Singly Linked List Defination  ============= 

# if you travel in one direction or a single direction, that 'Linked List' is called 'Singly Linked list'.. 

# that means if you travel form Head to Tail then it's called the 'Singly Linked List' ..




# ========== Doubly Linked List Defination ===========

# but here, in some Linked List we can also travel two direction 😎

# that means you can also travel from Head to Tail then you can also travel the opposite (backwards). 

# that means you can also travel from Tail to Head ..    
 
# || Note: the first Node of a Linked List is called the 'Head' and the last Node is called the 'Tail',
#   and the rest are called Nodes ||




# ========== informations which are exist in Doubly Linked List ===========

# A "Node" of a Doubly Linked List has three information:

#   1. Data or a Value 
#   2. Right pointer (Link to the next Node)  
#   3. Left pointer (Link to the previous Node)



#  ============ Circluar Linked List Defination ===========

# If the last node of a Linked List points towards the Head Node, || that Linked List is called the 'Circular Linked List' 😎


quz = input('''Which one is a Circular Linked List?
A. Linked List 
B. Two directional railway road for traveling
C. All friends making a circle and gossiping
:->> ''')

if quz == 'C':
    print('Correct Answer, Sir')
else:
    print('Wrong Answer, Sir')