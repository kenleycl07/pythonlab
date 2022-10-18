#########
### class
### Book
########

class Book:
    price = 9.99
    number_of_books = 0

    def __init__(self, name, number_of_pages, price):
        self.name = name
        self.number_of_pages = number_of_pages
        self.price = price
        Book.number_of_books += 1

    def change_price(self, prix):
        self.price = price

    def __str__(self):
        return 'Book : {}; {} pages; {} euros. '.format(self.name, self.number_of_pages, self.price)

# Create a Book object.
book1 = Book(name = 'Analytical Geometry', number_of_pages = 300, price = 10.99)
print(book1)
# Change the price.
book1..change_price(14.99)
print(book1)
# The value of the class variable price doesn't change.
print(Livre.prix)
# Create another Book object.
book2 = Book(name = 'Linear Algebra', number_of_pages = 400, price = 13.99)
print(book2)
# Display number of books.
print('Number of books:', Book.number_of_books)
