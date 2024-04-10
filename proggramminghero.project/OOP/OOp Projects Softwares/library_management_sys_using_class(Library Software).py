
class Libary:
   
    def __init__(self, name_of_library, list_of_books):
        self.name_library = name_of_library
        self.list_of_books = list_of_books
        self.lended_books = []
        self.usr_dict = {}
        self.donator_dict = {}

    
    def display_books(self):
        print("<< === Here are our books which are availble now === >>\n")
        for i in self.list_of_books:
            print(i, end=' || ')

    def lend_book(self, usr_nm, book_nm):
                                             # hence, we can use 'for' loop here, but we haven't used to keep the program shorter 😎 
        if book_nm in self.list_of_books:     # for i in self.list_of_books:
            print('<== Processing ==>')         # if i == book_nm:
            self.usr_dict[book_nm] = usr_nm         # print('Processing...'   
            self.list_of_books.remove(book_nm)      # self.list_of_books.remove(book_nm) 
            self.lended_books.append(book_nm)       # self.usr_dict[book_nm] = usr_nm
                                                # else:
                                                    # print('Sorry, Sir. The book is currently unavailble.')
            print('\nBook lending procceed. The', book_nm, 'book is now to user:', usr_nm)
        
        elif book_nm not in self.list_of_books:
            print('\nSorry, Sir. The book is currently unavailble.')

            if book_nm in self.usr_dict:
                print('The is now to the user:', self.usr_dict[book_nm])
            else:
                None
            
            # try:
            #     print('The book is now the to user:',self.usr_dict[book_nm])   | Alternative of the above |
            # except:
            #     pass

    def add_book(self, donater_nm, book_nm):

        self.donator_dict[book_nm] = donater_nm
        self.list_of_books.append(book_nm)
        print('Successfully added', book_nm, ', Donated by:', donater_nm)
        
    
    @staticmethod
    def thanking_met():
        print('''\n<< ==== Thanks for Staying with Us, Sir. Have a Nice Day ==== >>\n''')

books = ['ANNA', 'INVISIBLE', 'KARENINA','QUIXOTE', 'GRETA', 'GARBO', 'KARENINA','MOCKINGBIRD',
'KILL', 'MOCKINGBIRD', 'THE', 'GREAT', 'GATSBY', 'ONE', 'HUNDRED', 'YEARS', 'SOLITUDE',
'PASSAGE', 'INDIA', 'BELOVED']

# lib_nm = 'Hxd_Library Unit'
# hxd_library = Libary(lib_nm, books)

# hxd_library.display_books()

# hxd_library.lend_book(input('\nEnter user name: ').lower(), input('Enter book name: ').upper())
# print(hxd_library.usr_dict, hxd_library.list_of_books)

# hxd_library.add_book(input('\nEnter user name: ').lower(), input('Enter donating book name: ').upper())
# print(hxd_library.donator_dict, hxd_library.list_of_books)
# hxd_library.thanking_met()


lib = Libary('HxD_Libary', books)

def user_interFace():

    inpu = input('''
  < ==|| Enter 'A' to see OUr All Books ||== >
       ||   Enter 'L' to Lend Books   ||
       ||  Enter 'D' to Donate Books  ||
       || Enter 'AD' to see Donators  ||
       ||  Enter 'E' to Exit anytime  ||
       :: ''').upper()
        
    if inpu == 'E':
        lib.thanking_met()
        exit()
    if inpu == 'A':
        lib.display_books()

    elif inpu == 'L':
        lib.lend_book(input('Enter username: ').lower(), input('Enter Book Name: ').upper())

    elif inpu == 'D':
        lib.add_book(input('Enter Donator Name: ').lower(), input('Enter Book Name: ').upper())

    elif inpu == 'AD':
        if len(lib.donator_dict) == 0:
            print('Currently we Have no Donator')
        else:
            print('Donators:',lib.donator_dict)

    else:
        print('Sorry, Invaild Input')


while True:
    user_interFace()

