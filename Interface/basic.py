def main():
    from controller.control import LibrarySystem

    library_system = LibrarySystem

    print("\nLibrary Management System")
    print("Enter 'add' to Add Books")
    print("Enter 'cus' to Add Customers")
    print("Enter 'bor' Borrow a Book")
    print("Enter 'ret' to Return a Book")
    print("Enter 'avail' to Display Available Books")
    print("Enter 'borr' to Display Borrowed Books")
    print("Enter 'cust' to Display Customers")
    print("Enter 'borc' to Display Borrowed Books of a Customer")
    print("Enter 'delb' to delete a book from library")
    print("Enter 'delc' to delete a customer from library system")
    print("Enter 'exit' to Exit")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "add":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            library_system.add_book(title, author, genre)
            print("Book added successfully!")

        elif choice == "delb":
            book_id = int(input("Enter the book ID to delete: "))
            if library_system.delete_book(book_id):
                print("Book deleted successfully!")
            else:
                print("Failed to delete book. Please check the ID or try again later.")

        elif choice == "delc":
            cus_id = int(input("Enter the customer ID to delete: "))
            if library_system.delete_customer(cus_id):
                print("Customer deleted successfully!")
            else:
                print(
                    "Failed to delete Customer. Please check the ID or try again later."
                )

        elif choice == "cus":
            name = input("Enter the name of the customer: ")
            email = input("Enter the email of the customer: ")
            library_system.add_customer(name, email)
            print("Customer added successfully!")

        elif choice == "bor":
            customer_id = int(input("Enter the customer ID: "))
            book_id = int(input("Enter the book ID: "))
            if library_system.borrow_book(customer_id, book_id):
                print("Book borrowed successfully!")
            else:
                print("Failed to borrow book. Please check the IDs.")

        elif choice == "ret":
            customer_id = int(input("Enter the customer ID: "))
            book_id = int(input("Enter the book ID: "))
            if library_system.return_book(customer_id, book_id):
                print("Book returned successfully!")
            else:
                print("Failed to return book. Please check the IDs.")

        elif choice == "avail":
            available_books = library_system.get_available_books()
            print("Available Books:")
            for book in available_books:
                print(
                    f"ID: {book['_id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}"
                )

        elif choice == "borr":
            borrowed_books = library_system.get_borrowed_books()
            print("Borrowed Books:")
            for book in borrowed_books:
                print(
                    f"ID: {book['_id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}"
                )

        elif choice == "cust":
            customers = library_system.get_customers()
            print("Customers:")
            for customer in customers:
                print(
                    f"ID: {customer['_id']}, Name: {customer['name']}, Email: {customer['email']}"
                )

        elif choice == "borc":
            customer_id = int(input("Enter the customer ID: "))
            borrowed_books = library_system.get_customer_borrowed_books(customer_id)
            print("Books borrowed by the customer:")
            for book in borrowed_books:
                print(
                    f"ID: {book['_id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}"
                )

        elif choice == "exit":
            print("Exiting the Library Management")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
