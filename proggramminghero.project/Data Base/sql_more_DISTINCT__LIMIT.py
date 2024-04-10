import sqlite3

conn = sqlite3.connect('new.db')
cursor = conn.cursor()

# cursor.execute("CREATE TABLE Customers (Id INTEGER Primary Key, Email TEXT UNIQUE, District TEXT NOT NULL)")
# cursor.execute("INSERT INTO Customers VALUES(1, 'inc@gmail.com', 'Feni')")
# cursor.execute("INSERT INTO Customers VALUES(2, 'programming@outmail.com', 'Dhaka')")
# cursor.execute("INSERT INTO Customers VALUES(3, 'google@gmail.com', 'Chittagong')")
# cursor.execute("INSERT INTO Customers VALUES(4, 'microsoft@gmail.com', 'Dhaka')")
# cursor.execute("INSERT INTO Customers VALUES(5, 'ibm@outmail.com', 'Feni')")
# cursor.execute("INSERT INTO Customers VALUES(6, 'chrome@protonmail.com', 'California')")

# cursor.execute("SELECT * FROM Customers")
# data = cursor.fetchall()


#     ||||||||||||||||||||       DISTINCT      |||||||||||||||||| 

# now, let's say your manager told you to get the District names of our customers. Now, here are district name multiple times but we need to display one name just for once. 😎

# so, we can use "DISTINCT" keyword before the Column name to fetch one item for once.   (sounds like our Python's 'Set' 😁, cause it fetchs one data just for once.)

cursor.execute("SELECT DISTINCT District FROM Customers")

data = cursor.fetchall()

print(data)

 #           ||||||||||||||||          LIMIT          |||||||||||||||

print('\n')

# So, there are many or maybe thousands of Rows in a Table, But you want to see limited row, like first 10 or 20 or 50 or 100 whatever Columns, 
# here, you can you the "LIMIT" keyword after the Table name

cursor.execute("SELECT * FROM Customers LIMIT 4")
# cursor.execute("SELECT Email FROM Customers LIMIT 2")

limited_col = cursor.fetchall()
print(limited_col)

conn.commit()
conn.close()