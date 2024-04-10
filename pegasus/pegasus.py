# import os

# here the malicious code will be written and it will hack your data and uplaod on its author's server. 
# after that by executing the code below which is "os.remove('pegasus.py')" the pegasus malware will be automatically deleted !!!

# os.remove('pegasus.py')


at = [2, 4, 5, 6, 7, 9, 8, 17, 18]
sum_of_even = 0
even_list = []

for i in at:
    if i %2 == 0:
        even_list.append(i)
        sum_of_even +=  i
    else:
        continue

print(even_list)
print(sum_of_even)