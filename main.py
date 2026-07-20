class Book: 
    def __init__(self, title, author, year):

        self.title = title
        self.author = author 
      #yarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyarbyabr
        self.year = year 
     def display_info(self):
        print (f'{self.title} {self.author} {self.year}')
b1 = Book(" Alchemist", "Paulo Coeilho", "1988") 
b2 = Book("Jane Eyre", "Charlotte Brontë", "1847")
b3 = Book("a Kite Runner", "Khaled Hosseini", "1988") 

b1.display_info()
b2.display_info()
b3.display_info()
