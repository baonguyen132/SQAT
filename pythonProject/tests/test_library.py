import pytest
from src.library_app.book import Book
from src.library_app.member import Member
from src.library_app.library import Library


# Fixtures
@pytest.fixture
def library():
    return Library("Central Library")

@pytest.fixture
def book():
    return Book("Clean Code", "Robert Martin", "12345")

@pytest.fixture
def member():
    return Member("Alice", "M001")


# 1️⃣ Thêm sách thành công
def test_add_book(library, book):
    result = library.add_book(book)
    assert result is True
    assert book.isbn in library.books

# 2️⃣ Xóa sách có sẵn
def test_remove_existing_book(library, book):
    library.add_book(book)
    result = library.remove_book(book.isbn)
    assert result is True
    assert book.isbn not in library.books

# 3️⃣ Thử xóa sách không tồn tại
def test_remove_nonexistent_book(library):
    result = library.remove_book("99999")
    assert result is False

# 4️⃣ Thử xóa sách đang được mượn
def test_remove_borrowed_book(library, book, member):
    library.add_book(book)
    library.register_member(member)
    member.borrow_book(book)
    result = library.remove_book(book.isbn)
    assert result is False

# 5️⃣ Đăng ký thành viên thành công
def test_register_member(library, member):
    result = library.register_member(member)
    assert result is True
    assert member.member_id in library.members

# 6️⃣ Đăng ký thành viên với cùng ID
def test_register_member_duplicate(library, member):
    library.register_member(member)
    duplicate = Member("Bob", member.member_id)
    result = library.register_member(duplicate)
    assert result is False

# 7️⃣ Hủy đăng ký thành viên
def test_unregister_member(library, member):
    library.register_member(member)
    result = library.unregister_member(member.member_id)
    assert result is True
    assert member.member_id not in library.members

# 8️⃣ Thử hủy đăng ký thành viên không tồn tại
def test_unregister_nonexistent_member(library):
    result = library.unregister_member("M999")
    assert result is False

# 9️⃣ Thử hủy đăng ký thành viên đang mượn sách
def test_unregister_member_with_borrowed_books(library, book, member):
    library.add_book(book)
    library.register_member(member)
    member.borrow_book(book)
    result = library.unregister_member(member.member_id)
    assert result is False

# 🔟 Tìm kiếm sách theo tiêu đề, tác giả, ISBN
def test_find_books(library, book):
    library.add_book(book)
    # theo tiêu đề
    result = library.find_book("Clean Code")
    assert book in result
    # theo tác giả
    result = library.find_book("Robert Martin")
    assert book in result
    # theo ISBN
    result = library.find_book("12345")
    assert book in result
