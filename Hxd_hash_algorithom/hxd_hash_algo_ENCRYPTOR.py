def hxd_hash_algo(input_string):
    hash = ''
    for i in input_string:
        if i == 'A':
            hash += 'q'
        elif i == 'B':
            hash += 'y'
        elif i == 'C':
            hash += 'O'
        elif i == 'D':
            hash += 'i'
        elif i == 'E':
            hash += 't'
        elif i == 'F':
            hash += 'W'
        elif i == 'G':
            hash += 'T'
        elif i == 'H':
            hash += 's'
        elif i == 'I':
            hash += 'P'
        elif i == 'J':
            hash += '1'
        elif i == 'K':
            hash += 'd'
        elif i == 'L':
            hash += 'G'
        elif i == 'M':
            hash += 'w'
        elif i == 'N':
            hash += 'X'
        elif i == 'O':
            hash += '5'
        elif i == 'P':
            hash += 'S'
        elif i == 'Q':
            hash += 'h'
        elif i == 'R':
            hash += 'Q'
        elif i == 'S':
            hash += 'f'
        elif i == 'T':
            hash += '9'
        elif i == 'U':
            hash += 'R'
        elif i == 'V':
            hash += 'a'
        elif i == 'W':
            hash += 'P'
        elif i == 'X':
            hash += 'r'
        elif i == 'Y':
            hash += '8'
        elif i == 'Z':
            hash += 'c'
        elif i == 'a':
            hash += 'u'
        elif i == 'b':
            hash += 'x'
        elif i == 'c':
            hash += 'q'
        elif i == 'd':
            hash += 'U'
        elif i == 'e':
            hash += 'B'
        elif i == 'f':
            hash += 'V'
        elif i == 'g':
            hash += 'D'
        elif i == 'h':
            hash += '2'
        elif i == 'i':
            hash += 'F'
        elif i == 'j':
            hash += 'Y'
        elif i == 'k':
            hash += '7'
        elif i == 'l':
            hash += 'v'
        elif i == 'm':
            hash += 'Z'
        elif i == 'n':
            hash += 'A'
        elif i == 'o':
            hash += 'E'
        elif i == 'p':
            hash += 'K'
        elif i == 'q':
            hash += 'H'
        elif i == 'r':
            hash += 'L'
        elif i == 's':
            hash += '3'
        elif i == 't':
            hash += 'I'
        elif i == 'u':
            hash += 'g'
        elif i == 'v':
            hash += 'c'
        elif i == 'w':
            hash += 'e'
        elif i == 'x':
            hash += 'l'
        elif i == 'y':
            hash += 'C'
        elif i == 'z':
            hash += 'M'
        elif i == ' ':
            hash += '&'
        elif i == '.':
            hash += '^'
        elif i == '?':
            hash += '('
        elif i == ',':
            hash += '@'
        elif i == '!':
            hash += '-'
        elif i == '2':
            hash += ''

        

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
