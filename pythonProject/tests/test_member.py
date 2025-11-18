import pytest
from src.library_app.member import Member
from src.library_app.book import Book

# Fixtures
@pytest.fixture
def member():
    return Member("Alice", "M001")

@pytest.fixture
def sample_book():
    return Book("Clean Code", "Robert Martin", "12345")


# 1️⃣ Tạo thành viên thành công
def test_create_member_success():
    m = Member(name="Bob", member_id="M002")
    assert m.name == "Bob"
    assert m.member_id == "M002"
    assert m.borrowed_books == []

# 2️⃣ Tạo thành viên với các thuộc tính rỗng
def test_create_member_empty_fields():
    with pytest.raises(ValueError):
        Member(name="", member_id="M003")
    with pytest.raises(ValueError):
        Member(name="Charlie", member_id="")

# 3️⃣ Thành viên mượn một cuốn sách
def test_borrow_book(member, sample_book):
    result = member.borrow_book(sample_book)
    assert result is True
    assert sample_book in member.borrowed_books
    assert sample_book.is_borrowed is True

# 4️⃣ Thành viên trả một cuốn sách
def test_return_book(member, sample_book):
    member.borrow_book(sample_book)
    result = member.return_book(sample_book)
    assert result is True
    assert sample_book not in member.borrowed_books
    assert sample_book.is_borrowed is False

# 5️⃣ Thử mượn một cuốn sách không phải Book
def test_borrow_invalid_book(member):
    result = member.borrow_book("not a book")
    assert result is False

# 6️⃣ Thử trả một cuốn sách mà thành viên không mượn
def test_return_not_borrowed_book(member, sample_book):
    assert member.return_book(sample_book) is False

# 7️⃣ Kiểm tra danh sách sách đang mượn của thành viên
def test_get_borrowed_books(member, sample_book):
    member.borrow_book(sample_book)
    titles = member.get_borrowed_books()
    assert titles == ["Clean Code"]
