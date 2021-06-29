import os
class Library:
    __secret_key = os.environ.get("SECRET_LIB_KEY")
    __book_list = ['Игра Джералда', 'Четыре после полуночи', 'Сердца в Атлантиде', 'Зелёная миля', 'Лангольеры']

    @classmethod
    def book_list(cls, a, b):
        cls.__secret_key = a
        cls.__book_list = b
        for i in a:
            if a == 1:
                return b
            else:
                print("Forbidden action")

    @classmethod
    def give_book(cls, s, b, book_name):
        cls._secret_key = s
        cls._book_list = b
        cls.book_name = book_name
        for i in s:
            if s == 1:
                x = b - book_name
                return x
        else:
            print(f"Can't give this book {cls.book_name} to you ")
            return False

    @classmethod
    def return_book(cls, a, b, book_name):
        cls._secret_key = a
        cls._book_list = b
        cls.book_name = book_name
        for i in a:
            if a == 1 and b == 0:
                x = b + book_name
                return x
            else:
                print(f"Can't take this book {cls.book_name} from you")
