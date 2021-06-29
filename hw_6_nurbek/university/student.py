from library import Library
import  os

class Student:
    __name = 'Oskar'
    __public_key = os.environ.get("SECRET_PUB_KEY")
    books_taken = []

    @property
    def public_key(self):
        return self.__public_key

    @classmethod
    def get_book(cls, LibraryClass, book_name):
        cls.Library = LibraryClass
        cls.book_name = book_name

    @classmethod
    def return_book(cls, book_name):
        cls.book_name = book_name
        for i in Library.book_list:
            if book_name == Library.book_list:
                print("This books is already in Library")
