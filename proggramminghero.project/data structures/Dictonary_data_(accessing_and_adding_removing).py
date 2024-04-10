
# we have learnt already about the "dictionray datastructure", Dictionary can be declared by including a bunch of data pairs.........

dictorrny = {'algorithm' : 58, 'Tim' : 87, 'Johny' : 65, 'Silverhand' : 'Samurai'}

# printing or accessing or storing whole Dictionary..
print(dictorrny)
whole_dic = dictorrny
print(whole_dic)

# printing or acessing specific data from Dictionary...
print(dictorrny['algorithm'])
data = dictorrny['Johny']
print(data)

# adding new data in Dictionary, ''' just type the name of the Dictionary, then third paranthesis,
# type any 'key' which you want to add and close parenthesis, then equal sign and type the 'value'. like below...
dictorrny['V'] = 545
print(dictorrny)

# deleting data from a Dictionary, ''' just type 'del' and type name of Dictionary, then third parathesis and type 'key' of which data you want to delete or remove and close third parenthesis.

del dictorrny['Tim']
print(dictorrny)

# now one new thing, how to change the value of any 'key'? let's say the Dictionary Data Structure in the above is your friends game scores,
# so now think that 'Johny' scored 78 newly, and he want to change his score in the Dictionary, now what can you do?
# don't worry, very simple, it's the same method of 'adding new data in Dictionary', '''' just type the name of Dictionary, then third paranthesis,
# ''' then type the 'key' which value you want to change, here the 'Johny' and then euqal sign and type the new 'value', here that's 78 like below.....

dictorrny['Johny'] = 78
print(dictorrny)
