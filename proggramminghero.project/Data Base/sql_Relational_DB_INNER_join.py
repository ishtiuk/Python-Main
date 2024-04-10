#
# Think about 25 years advance from now. You will be married. You will have children, wife. Overall, a full family.
# now, let's say your family and some friends family have gone to a restrurant. 

# The resturant have a rule to, sit Children together on another table. And the olders in another sperate table. Now, each family's children have its own family's Id.

import sqlite3

conn = sqlite3.connect('Family.db')

cursor = conn.cursor()

# cursor.execute("CREATE TABLE Family_Table (Family_Id INTEGER PRIMARY KEY, Dad TEXT NOT NULL, Mom TEXT NOT NULL, Kid TEXT)")


# cursor.execute("INSERT INTO Family_Table VALUES(1111, 'Silverhand', 'Alt Cunningham', 'Spark')")
# cursor.execute("INSERT INTO Family_Table VALUES(1112, 'Jhon', 'Parker', 'Kiddi')")
# cursor.execute("INSERT INTO Family_Table VALUES(1113, 'Stephen', 'Lily', 'Judy')")
# cursor.execute("INSERT INTO Family_Table VALUES(1114, 'Hoking', 'Evelin', 'Parker')")
# cursor.execute("INSERT INTO Family_Table VALUES(1115, 'Kinchong', 'Mishy', 'Eyzwe')")
# cursor.execute("INSERT INTO Family_Table VALUES(1116, 'Edward', 'Mikoshy', 'Kiroshy')")
# cursor.execute("INSERT INTO Family_Table VALUES(1117, 'Vicky', 'Okala', 'Alexa')")
# cursor.execute("INSERT INTO Family_Table VALUES(1118, 'Silverhand', 'Alt Cunningham', 'Irfan')")
# cursor.execute("INSERT INTO Family_Table VALUES(1119, 'Silverhand', 'Alt Cunningham', 'Aftaf')")


#    |||||||||||||||||||||||           Normalization       ||||||||||||||||||||||||||

# Normalization means break down a big table into small tables or samller parts. 
# Normalization makes data easy to handle and changeble easily.......

# so, let's break down 😎

# cursor.execute("CREATE TABLE Parents (Family_Id INTEGER PRIMARY KEY, Dad TEXT NOT NULL, Mom TEXT NOT NULL)")

# cursor.execute("CREATE TABLE Kid_Table (Kids_Id INTEGER PRIMARY KEY, Kids_Name TEXT UNIQUE NOT NULL, Age INTEGER, Family_Id INTEGER)")



#   |||||||||||    Foreign Key |||||||||

# When you use the PRIMARY KEY of a table into another Table Column then, the second table column is called the "Foreign Key" column. Here we used the PRIMARY KEY of Parents TAble to identify them.
# In the "Kid_Table" every Kid holds their Family_Id to identify them.  ||||||||   So, the the column is "Foreign Key" column for the "Kid_Table" 😎



#   |||||||||||||||||||||   Denormalization  ||||||||||||||||

# Denormalization is acctually the opposite of Normalization 😅. In Normalization we have broken down the "Family_Table" into small two tables which are "Parents" and "Kid_Table" 😅.
# In the "Kid_Table" every Kid holds their Family_Id to identify them. 

# now, let's say today is Mom Day. So, we need to join the Moms from the "Parents" table and the Kids from the "Kid_Table", right?


# here comes the concept of joining Table

# |||||||||||||||   INNER JOIN     ||||||||| 
# Hence, there are many kinds of join. Here, we will use the INNER JOIN to join moms and kids together. 

# to create an INNER JOIN, you have to do three things: 
# 1. Write the Keyword "INNER JOIN"
# 2. Table with which you want JOIN
# 3. Matching columns from both tables

cursor.execute("SELECT Kids_Name, Mom FROM Kid_Table INNER JOIN Parents ON Parents.Family_Id = Kid_Table.Family_Id")

d = cursor.fetchall()
print(d)
# yeah got it.....!! 😁

conn.commit()
conn.close()

print("\n MOM Day Celebration\nKid_Name ---> Mom_Name\n")
for item in d:
    print(f"{item[0]} ---> {item[1]}")
