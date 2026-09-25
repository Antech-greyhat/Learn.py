class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return f"{self.title} is already borrowed"
        else:
            self.is_borrowed = True
            return f"You have borrowed {self.title}"

    def return_book(self):
        self.is_borrowed = False
        return f"You have returned {self.title}"

my_book = Book('Dune', 'Frank Herbert')
print(my_book.borrow())
print(my_book.borrow())      # should say already borrowed
print(my_book.return_book())
print(my_book.borrow())      # should succeed again, since it was returned

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def available_books(self):
        count = 0
        for book in self.books:
            if not book.is_borrowed:
                count += 1
        return count

my_library = Library('City Library')
my_library.add_book(my_book)
my_library.list_books()

book2 = Book('1984', 'George Orwell')
my_library.add_book(book2)

print(my_library.available_books())   # both books available → should be 2

my_book.borrow()
print(my_library.available_books())   # one borrowed now → should be 1