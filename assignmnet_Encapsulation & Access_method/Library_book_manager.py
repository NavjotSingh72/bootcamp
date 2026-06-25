class Book:
    def __init__(self, isbn, title, author, copies):
        self.__isbn = isbn          
        self._title = title         
        self._author = author       
        self.__copies = copies      

    @property
    def isbn(self):
        return self.__isbn

    @property
    def available(self):
        return self.__copies

    def checkout(self, n):
        if n <= 0:
            raise ValueError("Number of books must be positive")

        if n > self.__copies:
            raise ValueError("Not enough copies available")

        self.__copies -= n

    def return_book(self, n):
        if n <= 0:
            raise ValueError("Number of books must be positive")

        self.__copies += n


book = Book("9781234567890", "Python Basics", "John Smith", 5)

print("Available Copies:", book.available)

book.checkout(2)
print("After Checkout:", book.available)

book.return_book(1)
print("After Return:", book.available)