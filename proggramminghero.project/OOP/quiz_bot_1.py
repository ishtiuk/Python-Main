
quiz1 = input('''\nWhat is an Object?
A. Imaginary things in the inception world
B. Chairs and tables colored with yellow
C. Things with identifiable characteristics : ''')

quiz2 = input('''\nWhat are the two things every Object has/ can do?
A. Have price tags and round shapes
B. Have characteristics and can perform tasks
C. Can eat a burger on a romantic date : ''')

quiz3 = input('''\nAs a programmer, what will you call an Object template?
A. Trump plate
B. Object plate
C. Class : ''')

quiz4 = input('''\nWrite the appropriate keyword below.

______ Car:
    brand = 'Toyota'
my_car = Car() :: ''')

quiz5 = input('''\nHow will you create an app Object from your App class?

class App:
    title = 'Programming Hero'
    
my_app = _______  :: ''')

quiz6 = input('''\nHow would you access the title attribute from the my_app object?

class App:
    title = "Programming Hero"
my_app = App()
my_title = ______
print(my_title) : ''')

quiz7 = input('''\nCan attribute value be a List?
A. Yes
B. No
C. Sometimes :: ''')

full_mark = 70
mark = 0

if quiz1 == 'C' or quiz1 == 'c':
    mark += 10        
if quiz2 == 'B' or quiz2 == 'b':
    mark += 10
if quiz3 == 'C' or quiz3 == 'c':
    mark += 10
if quiz4 == 'class':
    mark += 10
if quiz5 == 'App()':
    mark += 10
if quiz6 == 'my_app.title':
    mark += 10
if quiz7 == 'A' or quiz7 == 'a':
    mark += 10

accuracy = (100 * (mark / 100))+30
print('you accuarcy rate is',accuracy,'%')





