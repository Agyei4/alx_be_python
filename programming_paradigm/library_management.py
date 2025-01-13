from IPython.core.release import author


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False # default value 
        
    
class Library:
    def __init__(self):
        self._books = [] 

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_checked_out:
                    print("Sorry, the book is already checked out.")
                else:
                    book.is_checked_out = True
                    print("You've checked out the book.")
                return
        print("Sorry, the book is not in the library.")

    def return_book(self, title): # ["return_book(self)"]
        for book in self._books:
            if book.title == title:
                if book.is_checked_out:
                    book.is_checked_out = False
                    print("You've returned the book.")
                else:
                    print("The book is not checked out.")
                return
        print("Sorry, the book is not in the library.") 

    def list_available_books(self):
        for book in self._books:
            if not book.is_checked_out:
                print(f"{book.title} by {author}")