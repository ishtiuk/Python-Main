def reverse_sting2(sentence):
    string = []
    final_line = ""
    for i in sentence:
        string.append(i)
    string.reverse()

    for char in string:
        final_line += char                                                                  # "final_line = char + final_line" this can be applied if 
                                                                                           # I don't write the "string.reverse()" on the first part.
    return final_line                                                                       # both method will perform same.

line = input()
print(reverse_sting2(line))
