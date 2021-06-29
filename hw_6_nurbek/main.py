import os
import cowsay
from hw_6_nurbek.university.library import Library
from hw_6_nurbek.university.student import Student

s = Student("Loksli")
d = Student("Artur")

print(books_list)

s.get_book(Library, "Сердца в Атлантиде")
d.get_book(Library, "Сердца в Атлантиде")

s.return_book(Library, "Сердца в Атлантиде")

print(books_list)

d.get_book(Library, "Сердца в Атлантиде")

print(books_list)


cowsay.tux("Well Done")