
first_q_ans = 'Root'
sec_q_ans = 'A root, one or more branches, and leaves'
third_q_ans = 'A list of friends who like superheroes'
fourth_q_ans = 'Binary Tree'
fifth_q_ans = 'Priority Queue'

marks = 0

first_q = input('What is the staring Node of a Tree DS?\nA. Head\nB. Node\nC. Root\nAns: ')
sec_q = input("\nWhat will you call the elements of a Tree DS?\nA. A tree, forest and some monkeys\nB. A root, one or more branches, and leaves\nC. Don't ask me, I am on a plant-based diet\nAns: ")
third_q = input("\nWhich one is not a Tree DS?\nA. A Folder structure in your computer\nB. A list of friends like superheroes\nC. A Family Tree that starts from your grandfather\nAns: ")
fourth_q = input("\nWhat type of Tree code has a maximum of two childern on each node?\nA. Double wood tree\nB. Money Tree\nC. Binary Tree\nAns: ")
fifth_q = input("\nWhich data Structures consider a priority?\nA. VIP Stack\nB. Priority Queue\nC. Platinum Tree\nAns: ")

if first_q == 'C':
    marks += 10
if sec_q == 'B':
    marks += 10
if third_q == 'B':
    marks += 10
if fourth_q == 'C':
    marks += 10
if fifth_q == 'B':
    marks += 10

final_marks = (100 * (marks/100))+50

print('your accuricy is :',final_marks,'%')