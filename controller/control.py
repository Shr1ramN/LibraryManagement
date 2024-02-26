class LibrarySystem:
    def __init__(self, mongo_connection):
        self.mongo_connection = mongo_connection
        self.books_collection = self.mongo_connection.books_collection
        self.customers_collection = self.mongo_connection.customers_collection
        self.book_id_counter = self.get_last_id(self.books_collection) + 1
        self.customer_id_counter = self.get_last_id(self.customers_collection) + 1

    def get_last_id(self, collection):
        last_item = collection.find_one({}, sort=[("_id", -1)])
        if last_item:
            return int(str(last_item["_id"]))
        return 0

    def add_book(self, title, author, genre):
        book = {
            "_id": self.book_id_counter,
            "title": title,
            "author": author,
            "genre": genre,
            "available": True,
        }
        self.books_collection.insert_one(book)
        self.book_id_counter += 1

    def delete_book(self, book_id):
        try:
            result = self.books_collection.delete_one({"_id": book_id})
            if result.deleted_count == 1:
                return True
            return False
        except Exception as e:
            print("An error occurred while deleting the book:", e)
        return False

    def add_customer(self, name, email):
        customer = {
            "_id": self.customer_id_counter,
            "name": name,
            "email": email,
            "borrowed_books": [],
        }
        self.customers_collection.insert_one(customer)
        self.customer_id_counter += 1

    def delete_customer(self, cus_id):
        try:
            result = self.customers_collection.delete_one({"_id": cus_id})
            if result.deleted_count == 1:
                return True
            return False
        except Exception as e:
            print("An error occurred while deleting the customer:", e)
        return False

    def borrow_book(self, customer_id, book_id):
        book = self.books_collection.find_one({"_id": book_id})
        if book and book.get("available", True):
            self.books_collection.update_one(
                {"_id": book_id}, {"$set": {"available": False}}
            )
            self.customers_collection.update_one(
                {"_id": customer_id}, {"$addToSet": {"borrowed_books": book_id}}
            )
            return True
        return False

    def return_book(self, customer_id, book_id):
        book = self.books_collection.find_one({"_id": book_id})
        if book and not book.get("available", True):
            self.books_collection.update_one(
                {"_id": book_id}, {"$set": {"available": True}}
            )
            self.customers_collection.update_one(
                {"_id": customer_id}, {"$pull": {"borrowed_books": book_id}}
            )
            return True
        return False

    def get_available_books(self):
        available_books = self.books_collection.find({"available": True})
        return list(available_books)

    def get_borrowed_books(self):
        borrowed_books = self.books_collection.find({"available": False})
        return list(borrowed_books)

    def get_customers(self):
        customers = self.customers_collection.find()
        return list(customers)

    def get_customer_borrowed_books(self, customer_id):
        customer = self.customers_collection.find_one({"_id": customer_id})
        if customer:
            borrowed_books_ids = customer.get("borrowed_books", [])
            borrowed_books = self.books_collection.find(
                {"_id": {"$in": borrowed_books_ids}}
            )
            return list(borrowed_books)
        return []