import sqlite3

# we have to execute dynamic queries. 

# like, inside software we'll take user's Email through some input and stored it in a variable called   "user_email".

user_email = input('Tell me about your Email: ')
user_friends = int(input('Tell me about your Friends number: '))

# there are three different ways to to create a Dynamic Query. One bad way is concatenate strings. But it increases the chance of getting Hacked..! 😒
# another way is to use Question mark (?) as a placeholder, but it's also less usefull 🙄

# one usefull way is to create a Dictionary>..

# type the full query as we want and just at the place of dynamic value, write a key. (Notice that while typing a 'key' in the query, you have to put a colon before the name
# of the 'key'. 
# 
# Hence, a dictionary key with a colon is the named 'Placeholder'), Like below...

conn = sqlite3.connect('another.db')

cursor = conn.cursor()

# cursor.execute("CREATE TABLE Users (Id INTEGER, Email TEXT, Password TEXT, Friends INTEGER)")
cursor.execute("INSERT INTO Users VALUES(1, 'ca@gmail.com', 'dHu5$', 200)")
cursor.execute("INSERT INTO Users VALUES(4, 'fran@outmail.com', 'fdfr4$', 50)")
# dic = {'email' : user_email}

cursor.execute("SELECT * From Users")# "Where Email = :email or Friends > :count", {'email' : user_email, 'count' : user_friends})

data = cursor.fetchall()
print(data)
conn.commit()
conn.close()