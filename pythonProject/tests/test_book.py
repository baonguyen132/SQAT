import pytest
from src.library_app.book import Book

def test_create_book():
    book = Book("Test Driven Development", "Kent Beck", "11111")
    assert book.title == "Test Driven Development"
    assert book.author == "Kent Beck"
    assert book.isbn == "11111"
    assert book.is_borrowed is False

def test_create_book_with_value_error():
    with pytest.raises(ValueError):
        Book("", "Kent Beck", "11111")
    with pytest.raises(ValueError):
        Book("Test Driven Development", "", "11111")
    with pytest.raises(ValueError):
        Book("Test Driven Development", "Kent Beck", "")

def test_borrow_available_book(book):
    result = book.borrow()
    assert result is True
    assert book.is_borrowed is True

def test_borrow_not_available_book(book):
    book.borrow()             # mượn lần 1 thành công
    result = book.borrow()    # mượn lần 2 không thành công
    assert result is False
    assert book.is_borrowed is True

def test_return_book(book):
    book.borrow()             # mượn trước khi trả
    result = book.return_book()
    assert result is True
    assert book.is_borrowed is False
