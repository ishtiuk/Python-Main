def palindrome_detector(sentence):
    palindrome_check_sntr = sentence[::-1]

    if sentence == palindrome_check_sntr:
        print("\n|| The sentence is palindrome ||")
    elif sentence != palindrome_check_sntr:
        print("\n|| This sentnce isn't palindrome ||")
    

    return "\n\n #|  ||Powered by HxD Corp||  |#\n\n" 

check_sentence = input("\n| Enter sentence to check palindrome | : ")
enterence_checkpoint = palindrome_detector(check_sentence)
print(enterence_checkpoint)