
keys = "abcdhijklmnopqrstuv efgwx!yz"
reversed_keys = keys[::-1]

special_keys = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
pairs = dict(zip(keys, reversed_keys))


def encoder_func(strings):
    encrypted = ""
    for char in strings:
        if char in pairs:
            encrypted += pairs[char]

    return encrypted

def decode_func(encoded_form):
    for i in encoded_form:
        if i in special_keys:
            encoded_form = encoded_form.replace(i, '')

    decrpyted = ""
    for char in encoded_form:
        if char in pairs:
            decrpyted += pairs[char]

    return decrpyted


usr_input = input('''
which one you want to do?__
Encode (E)
Decode (D)
:_> ''').upper().strip()

if usr_input == "E":
    data = input("Enter/paste string: ")

    en = encoder_func(data)
    print(f"Encrypted_/\n{en}")
    
elif usr_input == "D":
    data = input("Enter/paste encoded string: ")

    dc = encoder_func(data)
    print(f"Decrypted_/\n{dc}")

else:
    print("Invalid Input: ")

