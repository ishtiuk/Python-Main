import pyttsx3
import time

alsx = pyttsx3.init()

voices = alsx.getProperty('voices')
alsx.setProperty('voice', voices[1].id)

rate = alsx.getProperty('rate')
alsx.setProperty('rate', 180)

def talker(crdtal):
    alsx.say(crdtal)
    alsx.runAndWait()

Data_Structure = '''A Data Structure has three properties:.
1. Store more than one Data,
2. Special structure to store Data,
3. Special rule to add or remove data,'''
talker(Data_Structure)
talker("it's the characteristics of Data Structure")
time.sleep(0.5)

List = '''A List has a structure. You can put multiple data and has a specific way to add or remove data. That's why a list or array is a data structure'''
talker(List)
time.sleep(0.5)

Stack = '''When a Data Structure follows the Last in Fist Out (LIFO) policy, it is called a stack, example below.'''
stack_example = [1, 2, 85, 8]
stack_example.append(6)
stack_example.pop()
print(stack_example)
talker(Stack)
time.sleep(0.5)

Queue = 'When a Data Structure follows the First In first Out (FIFO) policy. It is called a Queue. Like waiting line, example below'
queue_example = [1, 2, 85, 8]
queue_example.append(4)
queue_example.pop(0)
print(queue_example)
talker(Queue)
time.sleep(0.5)

Dictionary = 'When a Data Structure contains Key-Value pairs, that data Structure is called a Dictionary. example below'
scores = {'John':58, 'Tim':84, 'Ben':46}
scores['Silverhand'] = 54
del scores['Tim']
print(scores)
talker(Dictionary)
time.sleep(0.5)

Linked_list = 'In a linked List, node use pointers to link with each other. While adding or removing a data or node, you must maintain the links in a Linked List. for more information check description about this in this Directory'
talker(Linked_list)
time.sleep(0.5)

Tree = 'When a Data Structure starts with a Root and each Node can have one or more childern, that Data Structure is called a Tree Data Structure. for more information check description about this in this Directory'
talker(Tree)
time.sleep(0.5)



using_DS = 'Use Data Structure to organize Data'
talker(using_DS)


