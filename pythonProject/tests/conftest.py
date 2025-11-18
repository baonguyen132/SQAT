import pytest

from src.library_app.book import Book
from src.library_app.library import Library
from src.library_app.member import Member


@pytest.fixture
def book():
    return Book("Test Driven Development", "Kent Beck", "11111")

def library():
    return Library("ABC")

def member():
    return Member(member_id="M001", name="Alice")