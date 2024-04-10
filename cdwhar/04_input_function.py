uniqe_item = []
lottery_list = [1,2,3,'godzilla', 5,8,6,8,68,58,68,'godzilla']
for i in lottery_list:
    if i not in uniqe_item:
        uniqe_item.append(i)
print(uniqe_item)