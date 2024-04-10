def reverse_string(sentence):
    str = ""
    for i in sentence: 
        str = i + str
    return str

sntns = input("Enter any sting: ")
print(reverse_string(sntns))