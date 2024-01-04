class Book:

    def __init__(self, id, title, author, year) -> None:
        self.id = id
        self.title = title
        self.year = year
        self.author = author


class LibrarySystem:

    def __init__(self) -> None:
        self.__books = []

    def insert_book(self, book: Book):
        self.__books.append(book)

    def list_books(self):
        return self.__books
    
def title():
    while True:
        try:
            title = str(input('Title of the book: '))
            if title == '':
                raise ValueError
            for letter in title:
                if not letter.isalpha() and not letter.isspace():
                    raise ValueError
        except:
            print('\033[31mOnly letters are accepted.\033[m')
        else:
            return title
        

def author():
    while True:
        try:
            author = str(input('Author of the book: ')).strip().title()
            if author == '':
                raise ValueError
            for letter in author:
                if not letter.isalpha() and not letter.isspace():
                    raise ValueError
        except:
            print('\033[31mOnly letters are accepted.\033[m')
        else:
            return author

def year():
    while True:
        try:
            year = str(input('Release year: ')).strip().title()
            if not year.isdigit():
                raise ValueError
        except:
            print('\033[31mONLY NUMBERS ARE ACCEPTED.\033[m')
        else:
            return year

def id():
    while True:
        try:
            id = str(input('Book ID: '))
            if not id.isdigit():
                raise ValueError
        except:
            print('\033[31mONLY NUMBERS ARE ACCEPTED.\033[m')
        else:
            return id


while True:
    print(f'\033[43m{"MAIN MENU":^100}\033[m')
    print(f'[1] INSERT A NEW BOOK\n[2] LIST BOOKS\n[3] QUIT')
    try:
        opt = int(input('Choose your option: '))
        assert opt >= 1 and opt <= 3
    except:
        print('\033[31mPLEASE, CHOOSE A VALID OPTION.\033[m')
    else:
        if opt == 1:
            livro1 = Book(id(), title(), author(), year())
            library_system = LibrarySystem()
            library_system.insert_book(livro1)
        elif opt == 2:
            try:
                books = library_system.list_books()
                print(f'\033[42m{"GEEK LIBRARY":^100}\033[m')
                print(f'{"ID":<5}{"TITLE":<50}{"AUTHOR":<40}{"YEAR":<5}')
                for book in books:
                    print(f'{book.id:<5}{book.title:<50}{book.author:<40}{book.year:<5}')
            except:
                print('\033[31mYOU DID NOT INSERT ANY BOOKS YET.\033[m')
        elif opt == 3:
            print('See you soon...')
            break