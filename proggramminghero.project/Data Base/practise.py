import sqlite3

conn = sqlite3.connect('monster.db')

cursor = conn.cursor()
# cursor.execute("CREATE TABLE EMP (Id INTEGER, Email TEXT, Password TEXT, Salary INTEGER)")

# quantity = int(input('Enter Employee numbers: '))

# for i in range(quantity):
#     info = input('''Enter Id Email Pwd Salary  | (separated with space) |
#     _ ''').split()

#     for item in info:
#         try:
#             indx = info.index(item)
#             item = int(item)
#             info[indx] = item
#         except:
#             pass

#     arg = f"{info[0]}, '{info[1]}', '{info[2]}', {info[3]}"
#     cursor.execute(f"INSERT INTO EMP VALUES({arg})")

#     cursor.execute("SELECT * FROM EMP")
#     cursor.execute("DELETE FROM EMP Where Password = 'dfkjk'")

cursor.execute("INSERT INTO EMP VALUES(1, 'Ca@gamil.com', '54$%6', 600)")
cursor.execute("INSERT INTO EMP VALUES(2, 'ty@gamil.com', '$%6', 500)")


# cursor.execute("UPDATE EMP SET Id = 3 Where Salary = 600")
# cursor.execute("UPDATE EMP SET Id = 4 Where Email = 'ty@gamil.com'")
# cursor.execute("DELETE FROM EMP Where Id > 2")
cursor.execute("SELECT * FROM EMP")
data = cursor.fetchall()
    
for row in data:
    print(row)

conn.commit()
conn.close()