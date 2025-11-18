from library_app.book import Book
from library_app.member import Member

class Library:
    def __init__(self, name):
        if not name:
            raise ValueError("Library name cannot be empty.")
        self.name = name
        self.books = {}  # ISBN -> Book object
        self.members = {} # Member ID -> Member object

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added to the library.")
        if book.isbn in self.books:
            return False # Book with this ISBN already exists
        self.books[book.isbn] = book
        return True

    def remove_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if not book.is_borrowed:
                del self.books[isbn]
                return True
            return False # Cannot remove borrowed book
        return False

    def register_member(self, member):
        if not isinstance(member, Member):
            raise TypeError("Only Member objects can be registered.")
        if member.member_id in self.members:
            return False # Member with this ID already exists
        self.members[member.member_id] = member
        return True

    def unregister_member(self, member_id):
        if member_id in self.members:
            member = self.members[member_id]
            if not member.borrowed_books:
                del self.members[member_id]
                return True
            return False # Cannot unregister member with borrowed books
        return False

    def find_book(self, search_term):
        results = []
        for book in self.books.values():
            if search_term.lower() in book.title.lower() or \
               search_term.lower() in book.author.lower() or \
               search_term == book.isbn:
                results.append(book)
        return results

    def __str__(self):
        return f"Library: {self.name} with {len(self.books)} books and {len(self.members)} members."