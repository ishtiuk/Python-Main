descrip = input("Enter text: ")
count = 0

for des in descrip:
    if des == " ":
        count += 1
count += 1
print("There are",count,"words") 