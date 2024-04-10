
import sqlite3

# first of all create connection with database. 
conn = sqlite3.connect('first.db')

cursor = conn.cursor()    # to execute qurires sequentually one by one

# to exectue querey add 'execute()' method to the 'cursor' function
# cursor.execute("CREATE TABLE Usr (Id INTEGER, Email TEXT, Password TEXT, Friends INTEGER)")       # use 'execute()' to run quries

# cursor.execute("""
# CREATE TABLE Usr (Id INTEGER,
#                   Email TEXT,                     # alternative
#                   Password TEXT
#                   Friends INTEGER)""")

cursor.execute('''
INSERT INTO Usr VALUES(1, 'modon@hotmail.com', 'tr$44', 200)''')

cursor.execute('''SELECT * FROM Usr''')

users = cursor.fetchall()       # to fetch all data 


conn.commit()   # to save changes which are created by Quries
# at last close connection
conn.close()



# inp = input('Enter Id, Email, password, Friends: ').split(' ')
# print(inp)

