import pytest

from src.library_app.book import Book
from src.library_app.library import Library
from src.library_app.member import Member


@pytest.fixture
def library():
    return Library("Central Library")

@pytest.fixture
def book():
    return Book("Clean Code", "Robert Martin", "12345")

@pytest.fixture
def member():
    return Member("Alice", "M001")