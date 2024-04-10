#
# basically, we make files to store data of program locally instead of database. Like if you made a Game, so you don't need a Database to store the high score, Right?
# Hence, you can store high score locally in a .txt file.


# 'r' gives the program to read only inside the  file.

# and 'r+' gives the program to read and write inside the file.

f = open("file.txt", 'r+')

f.write('hello program')

data = f.read()
print(data)

f.close()

f = open("file.txt", 'r+')

limited_Data = f.read(2)   # hence, we can set limit of read letters or bytes by passing number into  'read()' method.
print(limited_Data)

f.close()




# and we can read whole one line or sentence, by using the 'readline()' method.

f = open("file.txt", 'r+')

line = f.readline()

f.close()
print(line)




# and we can create binary files too..

binary = open('binyfile.bin', 'wb')

# f = binary.write()

binary.close()

# print(f)


# appending

f = open("file.txt", 'a')

f.write('\n Here we go')
f.close()


# both appending and reading

f = open("file.txt", 'a+')

f.write("\nHow are you?")
data = f.read()

f.close()

print(data)

