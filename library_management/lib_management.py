"""
1. Library Management System
    Description:
        - A system to manage book inventory in a library.
        
        Requirements:
        - Add, remove, and update books (title, author, genre).
        - Check-in and check-out functionality.
        - Search for books by title or author.
        - Track borrowed books and due dates (without real-time date tracking).
"""


# class LibraryManagementSystem:


import pickle
from datetime import datetime, timedelta

class LibraryManagementSystem:
    def __init__(self):
        self.books = (
            {}
        )

    def display_menu(self):
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Update Book")
        print("4. Loan Book")
        print("5. Return Book")
        print("6. View All Books")
        print("7. Exit")

    def add_book(self):
        book_id = input("Enter book ID: ")
        if book_id in self.books:
            print("This book ID already exists.")
        else:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            self.books[book_id] = {
                "title": title,
                "author": author,
                "is_borrowed": False,
            }
            print(f"Book '{title}' added successfully.")

    def remove_book(self):
        book_id = input("Enter book ID to remove: ")
        if book_id in self.books:
            del self.books[book_id]
            print("Book removed successfully.")
        else:
            print("Book ID not found.")

    def update_book(self):
        book_id = input("Enter book ID to update: ")
        if book_id in self.books:
            title = input("Enter new book title: ")
            author = input("Enter new book author: ")
            self.books[book_id] = {
                "title": title,
                "author": author,
                "is_borrowed": False,
            }
            print("Book updated successfully.")
        else:
            print("Book ID not found.")

    def loan_book(self):
        book_id = input("Enter book ID to loan: ")
        if book_id in self.books and not self.books[book_id]["is_borrowed"]:
            self.books[book_id]["is_borrowed"] = True
            due_date = datetime.now() + timedelta(days=14)  # Example: Due in 14 days
            self.books[book_id]["due_date"] = due_date.strftime("%Y-%m-%d")
            print(f"Book '{self.books[book_id]['title']}' loaned out. Due date: {self.books[book_id]['due_date']}")
        else:
            print("Book is not available for loan.")

    def return_book(self):
        book_id = input("Enter book ID to return: ")
        if book_id in self.books and self.books[book_id]["is_borrowed"]:
            self.books[book_id]["is_borrowed"] = False
            print(f"Book '{self.books[book_id]['title']}' returned.")
        else:
            print("Book is not currently loaned out.")

    def view_all_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks in Library:")
            for book_id, info in self.books.items():
                status = "Available" if not info["is_borrowed"] else f"Loaned Out, Due Date: {info['due_date']}"
                print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Status: {status}")

    def save_data(self):
        with open("library_data.pkl", "wb") as file:
            pickle.dump(self.books, file)

    def load_data(self):
        try:
            with open("library_data.pkl", "rb") as file:
                self.books = pickle.load(file)
        except FileNotFoundError:
            pass  # Ignore if the file is not found


def main():
    system = LibraryManagementSystem()
    system.load_data()  # Load existing data if available
    while True:
        system.display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            system.add_book()
        elif choice == "2":
            system.remove_book()
        elif choice == "3":
            system.update_book()
        elif choice == "4":
            system.loan_book()
        elif choice == "5":
            system.return_book()
        elif choice == "6":
            system.view_all_books()
        elif choice == "7":
            system.save_data()  # Save data before exiting
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

