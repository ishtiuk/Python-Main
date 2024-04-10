
writ = open('data.txt', 'w')
writ.write('hello nce')
writ.close()

red = open('data.txt', 'r')
data = red.read()
red.close()
print(data)
