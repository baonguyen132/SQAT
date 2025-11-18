class Book:
    def __init__(self, title, author, isbn):
        if not title or not author or not isbn:
            raise ValueError("Title, author, and ISBN cannot be empty.")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book: '{self.title}' by {self.author} (ISBN: {self.isbn}) - Status: {status}"