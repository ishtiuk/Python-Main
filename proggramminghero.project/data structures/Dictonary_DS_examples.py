#
# A big and ideal example of Dictionary Data Structure is your 'Phonebook' or 'Contacts' 😎

# it's very harder to save any Phone Number connected with a Name, Right?
# that cann't be saved using a List DS, it will be some harder to access or manipulate data correctly... 🙂


my_phonebook = {'V':56664, 'Jhonny':85555, 'Silver':97414, 'Judy':74555, 'Parker':72244}


# ============== Another Example: Store ==============

# Think about a fruit store you are running. So, every day you have to arrange fruits by row,
# and you have to remember the prices of every row's fruits...😏

price_of_fruits_for_store = {'mango': 500, 'lichi': 366,'pineapple': 422, 'banana': 155}

print('price of mango:', price_of_fruits_for_store['mango'])

# you can also change or update fruit's price 😎😎

price_of_fruits_for_store['mango'] = 687

print('now, price of mango:', price_of_fruits_for_store['mango'])


quz = input('''Which one of these is a good use case for a dictionary data structure?
A. Identify a friend's fake Facebook ID
B. Email addresses connected to name
C. Becoming a social media celebrity
:-->> ''').upper()

if quz == "B":
    print('Correct Answer, Sir')
else:
    print('Wrong Answer, Sir')