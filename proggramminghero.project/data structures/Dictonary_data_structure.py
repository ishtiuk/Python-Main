
# Dictonary is also a another type of Data Structure like the Stack and Queue. 
# A pair or relationship of data could be connected, Right?
# So, if one data is connected to another, it's called Dictionary Data Structure.
# a Dictionary has a pair of connected data.

# So, let's see how one data can be connected to another.

# ''''''''' pair of data ''''''

#                'Smasher' : 'Adam'            data can be connected to each other like this, first one data then ':' sign and then another data, in this case,
# the first data before ':' is called the 'Key' and the data after ':' is called 'Value'.
# here Smasher is Key and Adam is Value.

#  '''       Colletion of Data Pairs ''''''

# to declare a collection of data pairs, you will have to do two things:
# 1. Put all the pairs inside curly brackets '{}'.
# 2. Put a comman between the pairs, to sperate the keys and the values. 
# Like:

Dictionary_collection_of_data_pairs = {'algo' : 'fkd', 'hdt': 4, 5 : 54, 52.5 : 9.8}
element1 = Dictionary_collection_of_data_pairs['algo']
element2 = Dictionary_collection_of_data_pairs[5]
element3 = Dictionary_collection_of_data_pairs['hdt']
element4 = Dictionary_collection_of_data_pairs[52.5]

print(element1, element2, element3, element4)


# so, how to make a Dictionary?

# ''''' Dictionary Data '''''''''
# Dictionary Data Structure stores pairs of key-value......

# to declare a Dictionary Data Structure, you need 3 things:
# 1. A name of the Dictionary. (whatever you can give)
# 2. An equal sign.
# 3. A collection of data pairs.

Dictionary_data = {'iuo' : 'fkd', 'ertt': 4, 8 : 54, 87.54 : 9.8}
print(Dictionary_data)