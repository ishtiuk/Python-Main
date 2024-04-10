
import sqlite3

conn = sqlite3.connect('new.db')

cursor = conn.cursor()
# cursor.execute("CREATE TABLE User (Id INTEGER, Email TEXT, Password TEXT, Friends INTEGER)")
count = int(input('''How many Employee data want to enter?
_> '''))

for i in range(count):

    usrs = input('Enter Credintials_\nId Email Password Friends | separated by space |\n_> ').split(' ')

    # usrs = list(map(int, usrs))
    for i in range(len(usrs)):
        try:
            usrs[i] = int(usrs[i])
        except:
            pass
    print(usrs)

    cursor.execute("INSERT INTO User VALUES(:id, :email, :password, :friends)", {'id':usrs[0], 'email':usrs[1], 'password':usrs[2], 'friends':usrs[3]})

cursor.execute("SELECT * FROM User")

data = cursor.fetchall()
print(data)

conn.commit()
conn.close()


