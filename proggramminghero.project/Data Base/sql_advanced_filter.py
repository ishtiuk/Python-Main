import sqlite3

# we already know about filtering way for a Database, which is 'Where' clause 😎

conn = sqlite3.connect('another.db')
cursor = conn.cursor()

# let's say you have to you have to Select Rows for four ids. You can write ("SELECT * FROM Users Where Id = 2 or Id = 4 or Id = 3")

# but there is a better way, you can use the "IN" keyword 😏 inside the parethesis you can pass the all values. If any of the value is matched, that row will be Selected...

cursor.execute("SELECT * FROM Users Where Id IN (2, 4, 3)")


# now, let's say you have a Goldfish mind and you know that some of your database email last word is '@gmail.com' but you don't know the first one.
# what can you do now?   if you execute ("SELECT * FROM Users Where Email = '@gmail.com'"), then it will return error, because there are no email such like it.

# Hence you can use "Like" keyword instead of "=" if you know the something of data or email, like below...

cursor.execute("SELECT * FROM Users Where Email LIKE '%@gmail.com'")
data = cursor.fetchall()

print(data)

# now let's say, you know one users first email part, so find out that ... 😁😁

cursor.execute("SELECT * FROM Users Where Email LIKE 'ga%'")
data = cursor.fetchall()

print(data)