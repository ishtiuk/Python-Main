def adding_num_on_phonebook(num):
    phonebook_list = []
    for i in range(num):
        num = input("Enter phone number: ")                                    # here numbers will be added as string, because here are used only 'input()' not 'int(input())'
        phonebook_list.append(num)
    return phonebook_list
len_of_number = int(input("Enter how many numbers do you want to add: "))
print(adding_num_on_phonebook(len_of_number))  