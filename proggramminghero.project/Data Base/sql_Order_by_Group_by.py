   
            #    ||||||||||||||||||||||||||||||||           ORDER BY      |||||||||||||||||||||||

# to make sure you get things in the order by you want, you can add an Extra Keyword known as ORDER BY. After ORDER BY write the name of the column 😎

# if you want to order by the id, or email or friends whatever. 

import sqlite3


conn = sqlite3.connect('another.db')

cursor = conn.cursor()

# cursor.execute("SELECT * FROM Users ORDER BY Email")        # 
# cursor.execute("SELECT * FROM Users ORDER BY Id")

cursor.execute("SELECT * FROM Users ORDER BY Friends")
data = cursor.fetchall()

print(data)


#                    ||||||||||||||||||||      ORDER BY ASC and DESC      ||||||||||||||||||||| 

# after a Column name we can use an extra Keyword named " ASC ". 

# the ASC is short form of " Ascending ". It means you want the order to be smaller to larger. This means the column with the smallest value will be the top. If you keep going it will be increasing.

# and " DESC is the opposite of ASC"

# it will order the column from larger to smaller. :-D

cursor.execute("SELECT * FROM Users ORDER BY Id")

cursor.execute("SELECT * FROM Users ORDER BY Email DESC")
data = cursor.fetchall()

print(data)

cursor.execute("SELECT * FROM Users ORDER BY Friends ASC")
data = cursor.fetchall()

print(f"{data}\n\n")



#             ||||||||||||||||||||          GROUP BY       ||||||||||||||||

# Let's say you have a My_Playlist table. Where you have different singers name and their songs. Now, you want to " COUNT " the number of songs each singer have. 

# To do this you have to " GROUP BY " the songs by the singer column. 

conn = sqlite3.connect('My_Playlist.db')

cursor = conn.cursor()

# cursor.execute("CREATE TABLE My_Playlist (Song TEXT PRIMARY KEY, Singer TEXT NOT NULL)")
cursor.execute("SELECT Singer, COUNT(Song) FROM My_Playlist GROUP BY Singer")

datas = cursor.fetchall()
print(f'{datas}\n')

cursor.execute("SELECT * FROM MY_PLAYLIST")
d = cursor.fetchall()

for i in d:
    print(i)

conn.commit()
conn.close()


