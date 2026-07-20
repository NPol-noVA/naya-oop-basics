class Book:
    def __init__(self,name,author,year):

       self.name= name
       self.author = author

       self.year = year
class Library: 
    def __init__(self):
        self.books = []
        
    def add_book(self,book):
        self.books.append(book)

    def show_all(self):
        for k in self.books:
            print(f"Title: {k.name}")
            print(f"Author: {k.author}")
            print(f"Title: {k.year}")
			print()

          	
library = Library()
while True: 
    print("what is your book (0 to finish)") 
    b = input ("book: ").lower()
    if b == '0': 
	   
		break 
    print ("what is book author? (- if unknown)")
    t = input ("author: ").lower()
	print ('what is publishing year')	
    j = input ("year: ").lower()
    book = Book(b,t,j)
    library.add_book(book)
    print ('successful operation')
library.show_all() 
