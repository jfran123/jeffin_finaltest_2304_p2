#First part of the code
class Book:
    def __init__(self,title,publisher):
        self.title=title
        self.publisher=publisher
        
    
    def __str__(self):
        return f"{self.title} is published by {self.publisher}"
    
a = Book('Python Coding', 'McGrawHill') #constructor
print(a) #__str__ method
b = Book('Software Engineering', 'Wiley')
print(b)

# Second part of the code
class TextBook(Book):
    def __init__(self,title,publisher,can_borrow=True):
        super().__init__(title,publisher)
        self.can_borrow=can_borrow
    def __str__(self):
        return f"{self.title} published by {self.publisher} is {'borrowable' if self.can_borrow else 'not borrowable'}"
c = TextBook('Discrete Maths', 'Pearson')
#constructor with default can_borrow value
print(c) #__str__ method
d = TextBook('Human Anatomy', 'Macmillan', can_borrow=False)
#constructor with can_borrow set to False
print(d)

#Third part of the code
class ReferenceBook(Book):
    def __init__(self,title,publisher,is_ebook=True):
        super().__init__(title,publisher)
        self.is_ebook=is_ebook
    def __str__(self):
        return f"{self.title}, published by {self.publisher} ebook is {'available' if self.is_ebook else 'not available'}"
e = ReferenceBook('Communication English', 'Webster')
#constructor with default is_ebook value
print(e)
f = ReferenceBook('Database Concepts', 'McGrawHill', is_ebook=True)
#constructor with is_ebook set to True
print(f)
g = ReferenceBook('Bio Medical Instrumentation', 'Macmillan', is_ebook=False)
#constructor with is_ebook set to False
print(g)



# 2.0 Department
class Department:
    
    def __init__(self,name):
        self.name=name
        self.books=[]
    def __str__(self):
        return f"{self.name} Department have the following Books: {self.get_books()}."
    def add_book(self,book):
        self.books.append(book)
        # print(f"Adding {book.title} to {self.name} department")
    def get_books(self):
        return ", ".join(book.title for book in self.books)
        
#Test Input
infotech = Department('Information Technology') #constructor
infotech.add_book(a) #add_book method
infotech.add_book(b)
infotech.add_book(f)
print(infotech) #__str__ method and get_books method
med = Department('Medical') #constructor
med.add_book(d) #add_book method
med.add_book(g)
print(med)

maths = Department('Mathematics') #constructor
maths.add_book(c) #add_book method
print(maths)

eng = Department('English') #constructor
eng.add_book(e) #add_book method
print(eng)
