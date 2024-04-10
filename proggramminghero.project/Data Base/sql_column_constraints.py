#   

#           ||||||||||||||||||||||||||||||||             "NULL"      |||||||||||||||
# when creating table we can declare or command some rules, cause we are the maintance corpo of that DB 

# let's see, by default, every column of a Table accepts Null data. That means it will contain nothing. "Null" is for DataBase, similar to our python "None". 
# Both means nothing 😎

import sqlite3

conn = sqlite3.connect('our_database.db')

cursor = conn.cursor()

# cursor.execute("CREATE TABLE Customers (Id INTEGER, Email TEXT, District TEXT NOT NULL)")      # here, we declared the rule that the column should not accept any NULL Value. 😏
                                                                                               # if any user tries to enter "NULL", then database will return an exception.

# cursor.execute("INSERT INTO Customers VALUES(:id, :email, :district)", {'id': 1, 'email': 'proton@mail.com', 'district': None})
# here database retruned this when we tried to Enter "NULL" 😏 :  " sqlite3.IntegrityError: NOT NULL constraint failed: Customers.District " 😁

cursor.execute("INSERT INTO Customers VALUES(:id, :email, :district)", {'id': 1, 'email': 'proton@mail.com', 'district': 'CA'})

# conn.commit()
# conn.close()


#   |||||||||||||||||||||||||||||       "Unique"     ||||||||||||||||||||||||
# Another rule (constraint). We can apply the "UNIQUE" constraint. 
# now, what is it? Notice that we don't want to get duplicate email or one email used by multiple users, Right?
# one user can use one email just for once :

# so, if we declare the keyword "UNIQUE" after the column name like (Email column) while creating table, then every values of Email Column should be unique 😏, 
# database will not accept same Email multiple times  

# cursor.execute("CREATE TABLE un_tb (Id INTEGER, Email TEXT UNIQUE, Distict TEXT NOT NULL)")
# cursor.execute("INSERT INTO un_tb VALUES(:id, :email, :district)", {'id': 2, 'email':'xyz@mail.com', 'district': 'Nyc'})

# cursor.execute("INSERT INTO un_tb VALUES(:id, :email, :district)", {'id': 3, 'email':'xyz@mail.com', 'district': 'Nd'})

# we can see here this error, because email isn't unique 😏:  "sqlite3.IntegrityError: UNIQUE constraint failed: un_tb.Email"

# notice here, by defining UNIQUE the column will take 'email' NULL just for once, not more. Cause, if it will take NULL multiple times then it's Uniqueness will be gone 😏, simple logic. 

cursor.execute("select * from un_tb")

# conn.commit()
# conn.close()
 

#  ||||||||||||||||   "Primary Key"    |||||||||||||||||||

# there are another (constraint) named "Primary Key". This creates a unique ID. It's almost similar to unique. 
# Here, Primary Key constraints don't allow any NULL value. 

# and for one table there will be only one Primary Key. Primary Key is used to find a row very quickly 😁

cursor.execute("CREATE TABLE primary_key (Id INTEGER PRIMARY KEY, Email TEXT UNIQUE, Distict TEXT NOT NULL)")
cursor.execute("INSERT INTO primary_key VALUES(:id, :email, :district)", {'id': 1, 'email':'hjh@mail.com', 'district': 'Nyc'})
cursor.execute("INSERT INTO primary_key VALUES(:id, :email, :district)", {'id': 2, 'email':'xyz@mail.com', 'district': 'Nyc'})
cursor.execute("INSERT INTO primary_key VALUES(:id, :email, :district)", {'id': 3, 'email':'fgfg@mail.com', 'district': 'Nyc'})
cursor.execute("INSERT INTO primary_key VALUES(:id, :email, :district)", {'id': 4, 'email':'ccf@mail.com', 'district': 'Nyc'})

# if "Primary Key" has defined then it will not make same column data will same creditials 😏. Sounds very usefull 😎

cursor.execute("SELECT * FROM primary_key")

data = cursor.fetchall()
print(data)