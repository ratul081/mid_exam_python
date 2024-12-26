class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)


class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book '{self.__title}' borrowed successfully.")
        else:
            print(f"Error: Book '{self.__title}' is already borrowed.")

    def return_book(self):
        if self.__availability:
          print(f"Error: Book '{self.__title}' was not borrowed.")
        else:
            self.__availability = True
            print(f"Book '{self.__title}' returned successfully.")

    def view_book_info(self):
        if self.__availability:
          availability_status = "Available"
        else:
          availability_status = "Not Available"

        print(f"Book ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {availability_status}")

    @property
    def book_id(self):
        return self.__book_id

    @property
    def availability(self):
        return self.__availability


def main():
    Book("101", "The Hobbit", "J.R.R. Tolkien")
    Book("102", "Tomorrow", "George Orwell")
    Book("103", "To Kill a Mockingbird", "Harper Lee")
    Book("104", "Pride and Prejudice", "Jane Austen")
    Book("105", "1984", "George Orwell")
    Book("106", "Moby Dick", "Herman Melville")
    Book("107", "The Great Gatsby", "F. Scott Fitzgerald")
    Book("108", "War and Peace", "Leo Tolstoy")
    Book("109", "Crime and Punishment", "Fyodor Dostoevsky")
    Book("110", "The Catcher in the Rye", "J.D. Salinger")
    
    while True:
        print("\nMenu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            if Library.book_list:
                for book in Library.book_list:
                    book.view_book_info()
            else:
                print("No books available in the library.")

        elif choice == "2":
            book_id = input("Enter Book ID to borrow: ")
            book_found = False
            for book in Library.book_list:
                if book.book_id == book_id:
                    book.borrow_book()
                    book_found = True
                    break
            if not book_found:
                print("Error: Invalid Book ID.")

        elif choice == "3":
            book_id = input("Enter Book ID to return: ")
            book_found = False
            for book in Library.book_list:
                if book.book_id == book_id:
                    book.return_book()
                    book_found = True
                    break
            if not book_found:
                print("Error: Invalid Book ID.")

        elif choice == "4":
            print("Thanks for being with us!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
