import sqlite3


conn = sqlite3.connect('another.db')
cursor = conn.cursor()

usr_email = input('Enter Email: ')
usr_pwd = input('Enter pwd: ')


cursor.execute("SELECT * FROM Users Where Email = :email", {'email':usr_email})

data = cursor.fetchone()

if data is not None:
    f"Valid Email"
else:
    f"Invalid Email"


if data is not None and data[2] == usr_pwd:
    print('\n| Welcome Inside |\n')
else:
    print('\n| Wrong username or password |\n| Try Again |')


