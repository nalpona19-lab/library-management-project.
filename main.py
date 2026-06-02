import os


class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def display_book_info(self):
        print(f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Quantity: {self.quantity}")

    def check_availability(self):
        return self.quantity > 0

    def update_quantity(self, amount):
        self.quantity += amount


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):

        if book in self.borrowed_books:
            print("You already borrowed this book.")
            return

        if book.check_availability():
            self.borrowed_books.append(book)
            book.update_quantity(-1)
            print(f"{self.name} borrowed '{book.title}'")

        else:
            print("Book is not available.")

    def return_book(self, book):

        if book not in self.borrowed_books:
            print("This book was not borrowed by the user.")
            return

        self.borrowed_books.remove(book)
        book.update_quantity(1)

        print(f"{self.name} returned '{book.title}'")

    def view_borrowed_books(self):

        if not self.borrowed_books:
            print("No borrowed books.")
            return

        print(f"Books borrowed by {self.name}:")

        for book in self.borrowed_books:
            print("-", book.title)


class Library:

    def __init__(self):
        self.books = {}
        self.users = {}

    def load_books_from_file(self, filename):

        try:
            path = os.path.join(os.path.dirname(__file__), filename)

            with open(path, "r", encoding="utf-8") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 4:

                        book_id, title, author, quantity = data

                        self.books[int(book_id)] = Book(
                            int(book_id),
                            title,
                            author,
                            int(quantity)
                        )

            print("Books loaded successfully.")

        except FileNotFoundError:
            print("books.txt not found.")

    def add_book(self, book):

        if book.book_id in self.books:
            print("Book ID already exists.")
            return

        self.books[book.book_id] = book

        print("Book added successfully.")

    def remove_book(self, book_id):

        if book_id in self.books:
            del self.books[book_id]
            print("Book removed successfully.")

        else:
            print("Book ID not found.")

    def register_user(self, user):

        if user.user_id in self.users:
            print("User ID already exists.")
            return

        self.users[user.user_id] = user

        print("User registered successfully.")

    def list_books(self):

        if not self.books:
            print("No books available.")
            return

        for book in self.books.values():
            book.display_book_info()

    def list_users(self):

        if not self.users:
            print("No users registered.")
            return

        for user in self.users.values():
            print(f"ID: {user.user_id} | Name: {user.name}")

    def search_book_by_id(self, book_id):
        return self.books.get(book_id)

    def search_book_by_title(self, title):

        results = []

        for book in self.books.values():

            if title.lower() in book.title.lower():
                results.append(book)

        return results

    def show_statistics(self):

        print("\n===== LIBRARY STATISTICS =====")

        print("Total Books:", len(self.books))
        print("Total Users:", len(self.users))


def main():

    library = Library()

    library.load_books_from_file("books.txt")

    library.register_user(User(1, "Geek_1"))
    library.register_user(User(2, "Geek_2"))

    while True:

        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")

        print("1. View All Books")
        print("2. Search Book by Title")
        print("3. Search Book by ID")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View Borrowed Books")
        print("7. Add New Book")
        print("8. Remove Book")
        print("9. Add New User")
        print("10. View All Users")
        print("11. Library Statistics")
        print("12. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            library.list_books()

        elif choice == "2":

            title = input("Enter title: ")

            books = library.search_book_by_title(title)

            if books:

                for book in books:
                    book.display_book_info()

            else:
                print("Book not found.")

        elif choice == "3":

            book_id = int(input("Enter Book ID: "))

            book = library.search_book_by_id(book_id)

            if book:
                book.display_book_info()

            else:
                print("Book not found.")

        elif choice == "4":

            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID: "))

            user = library.users.get(user_id)
            book = library.books.get(book_id)

            if user and book:
                user.borrow_book(book)

            else:
                print("Invalid User ID or Book ID.")

        elif choice == "5":

            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID: "))

            user = library.users.get(user_id)
            book = library.books.get(book_id)

            if user and book:
                user.return_book(book)

            else:
                print("Invalid User ID or Book ID.")

        elif choice == "6":

            user_id = int(input("Enter User ID: "))

            user = library.users.get(user_id)

            if user:
                user.view_borrowed_books()

            else:
                print("User not found.")

        elif choice == "7":

            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            quantity = int(input("Enter Quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.")

            else:
                library.add_book(
                    Book(book_id, title, author, quantity)
                )

        elif choice == "8":

            book_id = int(input("Enter Book ID to remove: "))

            library.remove_book(book_id)

        elif choice == "9":

            user_id = int(input("Enter User ID: "))
            name = input("Enter Name: ")

            library.register_user(
                User(user_id, name)
            )

        elif choice == "10":

            library.list_users()

        elif choice == "11":

            library.show_statistics()

        elif choice == "12":

            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()