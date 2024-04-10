marks = 0

q1 = input('''Which policy does a Stack follow?
A. FIFO, B. LIFO, C. FIBO. : ''')
print('\n')

q2 = input('''Is List a Data Structure?
A. Yes, B. NO, C, Maybe. : ''')
print('\n')

q3 = input('''How would you add ketchup in the food stack?
food = ['buger','fried']
food._______('ketchup')
print(food) : ''')
print('\n')

q4 = input('''What is a Data Sturcture?
A. A building structure to go for a tour. B. A Structure to store, manipulate and use date, C. A process of getting kicked out of a school. : ''')
print('\n')

q5 = input('''What would be the right parameter inside pop to remove an element from a queue below?
badBoys = ['Suny','jimmy','silverhand']
kicked = badBoys.pop()
print(kicked) : ''')
print('\n')

q6 = input('''We have a Dictionary of students IDs which pair with student name. Now, add a new student ID 7 whose value will be Ariana.
students = {12: 'Gaga', 81: 'Madona'}
students[___] = 'Ariana'
print(students) : ''')
print('\n')

q7 = input('''What is the first element of a Linked List called?
A. Root, B. Head, C. Tail. : ''')
print('\n')

q8 = input('''Which one is not a Tree Data Structure?
A. A Folder structure in your computer,
B. A List of friends who likes superheroes,
C. A Family Tree that starts from your grandfather : ''')
print('\n')

q9 = input('''When you remove an element from a queue, which element goes out?
A. The first one,
B. The last one,
C. The crazy one : ''')
print('\n')

q10 = input('''What is maximum number of children a binary treee node can have?
A. One,
B. Two,
C. Twenty Two : ''')
print('\n')


if q1 == 'B':
    marks += 10

if q2 == 'A':
    marks += 10

if q3 == 'append':
    marks += 10

if q4 == 'B':
    marks += 10

if q5 == '0':
    marks += 10

if q6 == '7':
    marks += 10

if q7 == 'B':
    marks += 10

if q8 == 'B':
    marks += 10

if q9 == 'A':
    marks += 10

if q10 == 'B':
    marks += 10

accuracy = 100 * (marks/100)

print('your accuracy: ', accuracy)
