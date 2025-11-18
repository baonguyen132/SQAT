import pytest
from src.library_app.book import Book

# 1️⃣ Tạo sách thành công
def test_create_book():
    book = Book("Test Driven Development", "Kent Beck", "11111")
    assert book.title == "Test Driven Development"
    assert book.author == "Kent Beck"
    assert book.isbn == "11111"
    assert book.is_borrowed is False

# 2️⃣ Tạo sách với thuộc tính rỗng -> ValueError
def test_create_book_with_value_error():
    with pytest.raises(ValueError):
        Book("", "Kent Beck", "11111")
    with pytest.raises(ValueError):
        Book("Test Driven Development", "", "11111")
    with pytest.raises(ValueError):
        Book("Test Driven Development", "Kent Beck", "")

# 3️⃣ Mượn sách có sẵn
def test_borrow_available_book():
    book = Book("Clean Code", "Robert Martin", "22222")
    result = book.borrow()
    assert result is True
    assert book.is_borrowed is True

# 4️⃣ Mượn sách đã được mượn -> trả về False
def test_borrow_not_available_book():
    book = Book("Refactoring", "Martin Fowler", "33333")
    book.borrow()             # mượn lần 1 thành công
    result = book.borrow()    # mượn lần 2 không thành công
    assert result is False
    assert book.is_borrowed is True

# 5️⃣ Trả một cuốn sách đã mượn
def test_return_book():
    book = Book("Domain-Driven Design", "Eric Evans", "44444")
    book.borrow()             # mượn trước khi trả
    result = book.return_book()
    assert result is True
    assert book.is_borrowed is False
