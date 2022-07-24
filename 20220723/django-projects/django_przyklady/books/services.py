from abc import abstractmethod, ABC
from typing import List

from books.utils import read_from_csv, Book


class BookProvider(ABC):

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def get_book(self, id) -> Book:
        pass


class BookCsvProvider(BookProvider):

    def get_all_books(self) -> List[Book]:
        books = read_from_csv("books/data/data.csv")
        return books

    def get_book(self, id) -> Book:
        books = read_from_csv("books/data/data.csv")
        return books[id-1]


class ModelsBooksProvider(BookProvider):

    def get_all_books(self) -> List[Book]:
        pass

    def get_book(self, id) -> Book:
        pass


class BookService:

    def __init__(self, provider: BookProvider):
        self.provider = provider

    def get_all_books(self) -> List[Book]:
        return self.provider.get_all_books()

    def get_book(self, book_id) -> Book:
        return self.provider.get_book(book_id)


provider = BookCsvProvider()
book_service = BookService(provider=provider)