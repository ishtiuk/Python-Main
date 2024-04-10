def item_input():
    items = []
    lenght = int(input("How many element do you want to enter: "))
    for i in range(lenght):
        item = int(input("Enter your elements in integer format: "))
        items.append(item)
    return items

def duplicate_itemrm(list_num):
    unique = []
    for i in list_num:
        if i not in unique:
            unique.append(i)
    return unique

list_sum = item_input()
print("here you unique list: ", duplicate_itemrm(list_sum))