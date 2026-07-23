class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_all(self):
        if not self.books:
            print("No books in the library.")
            return

        for book in self.books:
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Year: {book.year}")
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"Status: {status}")
            print()

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print("This book has been successfully borrowed.")
                else:
                    print("This book is already borrowed.")
                return

        print("This book is not available in the library.")

    def returning_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print("The book has been returned successfully.")
                else:
                    print("This book was not borrowed.")
                return

        print("This book does not exist in the library.")


library = Library()

while True:
    print("Enter your book (0 to finish)")
    b = input("Book: ").lower()

    if b == "0":
        break


	
    print("What is the book author? ( if unknown)")
    t = input("Author: ").lower()

    print("What is the publishing year?")
    y = input("Year: ")

    book = Book(b, t, y)
    library.add_book(book)

    print("successful operation")

library.show_all()

while True:
    print("Choose what you want:")
    print("1. Borrow book")
    print("2. Return book")
    print("3. Show all books")
    print("4. Exit")

    try:
        x = int(input("Enter your choice: "))

        if x == 1:
            s = input("Book Title: ").lower()
            library.borrow_book(s)

        elif x == 2:
            s = input("Book Title: ").lower()
            library.returning_book(s)

        elif x == 3:
            library.show_all()

        elif x == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

    except ValueError:
        print("Please enter a valid number.")
