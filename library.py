class Library:
    def __init__(self):
        self.Books = []

    def add_books(self, title):
        self.Books.append(title)

    def take_book(self, title, student):
        for i in self.Books:
            if i == title:
                self.Books.remove(title)
                print('"' + title + '"' + " is taken by " + student.full_name)
                student.student_books.append(title)
                return student.student_books
                break
            else:
                print("No such book in the Library")
                return

    def return_book(self, title, student):
        for i in student.student_books:
            if title == i:
                self.Books.append(title)
                student.student_books.remove(title)
                print('"' + title + '"' + " has been returned to the library by " + student.full_name)
                break
            else:
                print("Please check your spelling")

    def get_books(self):
        print("Books available in the library are: ", self.Books)


class Student:
    def __init__(self, full_name):
        self.full_name = full_name
        self.student_books = []


StudLib = Library()
StudLib.get_books()
StudLib.add_books("OOAD")
StudLib.add_books("Learning Python")
StudLib.add_books("Effective Python")
StudLib.add_books("Clean Code")
StudLib.add_books("OOAD")
StudLib.get_books()
Shush = Student("Shush")
Ani = Student("Ani")
StudLib.take_book("OOAD", Shush)
StudLib.get_books()
StudLib.take_book('War and Peace', Shush)
StudLib.take_book("Learning Python", Ani)
StudLib.get_books()
StudLib.return_book("OOP", Shush)
StudLib.return_book("OOAD", Shush)
StudLib.get_books()
StudLib.return_book("Learning Python", Ani)
StudLib.get_books()
