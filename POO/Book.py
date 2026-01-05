class Book:
    def __init__(self="Sin catalogar", title="Sin Catalogar", author="Sin Catalogar", editorial="Sin Catalogar", release_year=0, isbn = "Sin catalogar", num_pages = 0, prize = 0.0, amount = 0):
        self.title = title
        self.author = author
        self.editorial = editorial
        self.release_year = release_year
        self.isbn = isbn
        self.num_pages = num_pages
        self.prize = prize
        self.amount = amount

    def show_info(self):
        return f"Book [title:{self.title}, author:{self.author}, editorial:{self.editorial}, releaseYear:{self.release_year}, isbn:{self.isbn}, numPages:{self.num_pages}, prize:{self.prize}, amount:{self.amount}]"

    def __str__(self):
        return self.show_info()