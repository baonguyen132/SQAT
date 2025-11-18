from src.library_app.book import Book


class Member:
    def __init__(self, name, member_id):
        if not name or not member_id:
            raise ValueError("Name and member ID cannot be empty.")
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if isinstance(book, Book) and book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if isinstance(book, Book) and book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

    def get_borrowed_books(self):
        return [book.title for book in self.borrowed_books]

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"