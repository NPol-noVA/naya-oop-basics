class Book:
    def __init__(self,name,author):

       self.name= name
       self.author = author

class Library: 
    def __init__(self):
        self.books = []
        
    def add_book(self,book):
        self.books.append(book)

    def show_all(self):
        for k in self.books:
            print(f"Title: {k.name}")
            print(f"Author: {k.author}")
            print()

          	
library = Library()
while True: 
    print("what is your book (0 to finish)") 
    b = input ("book: ")
    if b == '0': 
	    break 
    print ("what is book author?")
    t = input ("author: ")
    book = Book(b,t)
    library.add_book(book)
    
library.show_all() 
