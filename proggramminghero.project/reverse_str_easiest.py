def reverse_str_easiest(sentence):
    print(sentence[::-2])
    reversed = sentence[::-1]
    return reversed

print(reverse_str_easiest(input("Enter your sentence to reverse: ")))