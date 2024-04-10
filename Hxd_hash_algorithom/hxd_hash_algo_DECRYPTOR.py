def hxd_hash_algo(input_string):
    hash = ''
    for i in input_string:
        if i == 'q':
            hash += 'A'
        elif i == 'y':
            hash += 'B'
        elif i == 'O':
            hash += 'C'
        elif i == 'i':
            hash += 'D'
        elif i == 't':
            hash += 'E'
        elif i == 'W':
            hash += 'F'
        elif i == 'T':
            hash += 'G'
        elif i == 's':
            hash += 'H'
        elif i == 'P':
            hash += 'I'
        elif i == '1':
            hash += 'J'
        elif i == 'd':
            hash += 'K'
        elif i == 'G':
            hash += 'L'
        elif i == 'w':
            hash += 'M'
        elif i == 'X':
            hash += 'N'
        elif i == '5':
            hash += 'O'
        elif i == 'S':
            hash += 'P'
        elif i == 'h':
            hash += 'Q'
        elif i == 'Q':
            hash += 'R'
        elif i == 'f':
            hash += 'S'
        elif i == '9':
            hash += 'T'
        elif i == 'R':
            hash += 'U'
        elif i == 'a':
            hash += 'V'
        elif i == 'p':
            hash += 'W'
        elif i == 'r':
            hash += 'X'
        elif i == '8':
            hash += 'Y'
        elif i == 'c':
            hash += 'Z'
        elif i == 'u':
            hash += 'a'
        elif i == 'x':
            hash += 'b'
        elif i == 'q':
            hash += 'c'
        elif i == '2':
            hash += 'h'
        elif i == 'U':
            hash += 'd'
        elif i == 'B':
            hash += 'e'
        elif i == 'V':
            hash += 'f'
        elif i == 'D':
            hash += 'g'
        elif i == 'F':
            hash += 'i'
        elif i == 'Y':
            hash += 'j'
        elif i == '7':
            hash += 'k'
        elif i == 'v':
            hash += 'l'
        elif i == 'Z':
            hash += 'm'
        elif i == 'A':
            hash += 'n'
        elif i == 'E':
            hash += 'o'
        elif i == 'K':
            hash += 'p'
        elif i == 'H':
            hash += 'q'
        elif i == 'L':
            hash += 'r'
        elif i == '3':
            hash += 's'
        elif i == 'I':
            hash += 't'
        elif i == 'g':
            hash += 'u'
        elif i == 'c':
            hash += 'v'
        elif i == 'e':
            hash += 'w'
        elif i == 'l':
            hash += 'x'
        elif i == 'C':
            hash += 'y'
        elif i == 'M':
            hash += 'z'
        elif i == '&':
            hash += ' '
        elif i == '^':
            hash += '.'
        elif i == '(':
            hash += '?'
        elif i == '@':
            hash += ','
        elif i == '-':
            hash += '!'

        

    return hash

text = input()
print(hxd_hash_algo(text))


# inp = input("Enter your hash: ")
# print('\n')
# print("Decrypting...")
# # time.sleep(3)
# print('\n')
# print(hxd_hash_algo(inp))
# print('\n')
