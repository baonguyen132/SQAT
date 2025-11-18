import pytest
from src.library_app.member import Member
from src.library_app.book import Book


def test_create_member_success():
    m = Member(name="Bob", member_id="M002")
    assert m.name == "Bob"
    assert m.member_id == "M002"
    assert m.borrowed_books == []

def test_create_member_empty_fields():
    with pytest.raises(ValueError):
        Member(name="", member_id="M003")
    with pytest.raises(ValueError):
        Member(name="Charlie", member_id="")

def test_borrow_book(member, book):
    result = member.borrow_book(book)
    assert result is True
    assert book in member.borrowed_books
    assert book.is_borrowed is True

def test_return_book(member, book):
    member.borrow_book(book)
    result = member.return_book(book)
    assert result is True
    assert book not in member.borrowed_books
    assert book.is_borrowed is False

def test_borrow_invalid_book(member):
    result = member.borrow_book("not a book")
    assert result is False

def test_return_not_borrowed_book(member, book):
    assert member.return_book(book) is False

def test_get_borrowed_books(member, book):
    member.borrow_book(book)
    titles = member.get_borrowed_books()
    assert titles == ["Clean Code"]
