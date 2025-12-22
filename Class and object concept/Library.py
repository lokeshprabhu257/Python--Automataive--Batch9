class Library:
    def __init__(self, book_title, book_author):
        self.book_title = book_title
        self.book_author = book_author

    def book_info(self):
        print("Book Title :", self.book_title)
        print("Author     :", self.book_author)


# creating two book objects 
book1 = Library("The Secret Garden", "Frances Hodgson Burnett")
book2 = Library("Wings of Fire", "A.P.J. Abdul Kalam")

# displaying details
book1.book_info()
print("**************************************")
book2.book_info()