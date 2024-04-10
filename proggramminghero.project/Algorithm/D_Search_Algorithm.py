
# Supose that we have Lost your PHone's charger in your Room. Now, what you will do now?  

# you will search it IN your Backpack, then in YOur Bathroom, then under your Bed. 🥴🥴


#  Linear Search ..

# so, you have followed some sequentially steps for searching your Charger. it's a step by step process.  so, it was a Linear Search


quez = input('''What is a Search Algorithm?
A. Step by step process to find elements
B. A process to find a phone charger
C. Some kind of allergy-related
-->> ''').upper()
if quez == 'A':
    print('Correct answer, Sir')
else: 
    print('Wrong Answer, Sir')


# example of Linear Search 

nums = [10, 4, 53, 533, 64, 3, 69, 90]
serach = 533

for num in nums:
    if num == serach:
        print('I got the number:', serach)

