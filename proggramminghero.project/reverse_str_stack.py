def reverse_stirng_stack(line):
    word_list = []
    
    for i in line:
        word_list.append(i)

    sentence = ""
    while len(word_list) > 0:
        last = word_list.pop()
        sentence += last

    return sentence

sentence = input("Enter your sentence: ")
stnc = reverse_stirng_stack(sentence)
print(stnc)