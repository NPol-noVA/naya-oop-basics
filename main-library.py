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
	

    def borrow_book (self, title):
        k = 0
        for j in self.books:
            if j.title == title and j.is_borrowed == False:
                print ("This book is available and it is successfully borrowed")
               
				j.is_borrowed = True
                k = 1
        if k == 0:
            print ("This book isn't available now")
	def returning_book(self, title):
        k = 0  
        for j in self.books:
            if j.title == title and j.is_borrowed :
                j.is_borrowed = False
                k = 1 
        
		 if k ==0 : 
            print ("This book isn't borrowed from this library ") 
                  	
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
print ("if you want to borrow a book enter 1")
x = int (input())
if x == 1:
	s = input("Book Title:").lower()
	borrow_book(s)

    
