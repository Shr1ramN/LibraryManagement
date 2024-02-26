from fastapi import FastAPI, HTTPException
from controller.control import LibrarySystem
from imports.mongo import MongoDBConnection

app = FastAPI(
    title="Library Management System",
    description="Library Management App which has a good future i think",
    contact={
        "name": "Shriram Narayana",
        "url": "http://shr1ram.me",
        "email": "s@s.com",
    },
    openapi_tags=[
        {
            "name": "Books",
            "description": "Operations related to books in the library",
        },
        {
            "name": "Customers",
            "description": "Operations related to customers in the library",
        },
    ],
)

# Connect to MongoDB
mongo_connection = MongoDBConnection(host="localhost", port=27017)
library_system = LibrarySystem(mongo_connection)


@app.post("/books/", tags=["Books"])
def create_book(title: str, author: str, genre: str):
    """Create a new book."""
    library_system.add_book(title, author, genre)
    return {"message": "Book added successfully"}


@app.delete("/books/{book_id}/", tags=["Books"])
def delete_book(book_id: int):
    """Delete a book by ID."""
    if library_system.delete_book(book_id):
        return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/customers/", tags=["Customers"])
def create_customer(name: str, email: str):
    """Create a new customer."""
    library_system.add_customer(name, email)
    return {"message": "Customer added successfully"}


@app.delete("/customers/{customer_id}/", tags=["Customers"])
def delete_customer(customer_id: int):
    """Delete a customer by ID."""
    if library_system.delete_customer(customer_id):
        return {"message": "Customer deleted successfully"}
    raise HTTPException(status_code=404, detail="Customer not found")


@app.post("/borrow/", tags=["Books"])
def borrow_book(customer_id: int, book_id: int):
    """Borrow a book by customer ID and book ID."""
    if library_system.borrow_book(customer_id, book_id):
        return {"message": "Book borrowed successfully"}
    raise HTTPException(
        status_code=404, detail="Book or customer not found or book is not available"
    )


@app.post("/return/", tags=["Books"])
def return_book(customer_id: int, book_id: int):
    """Return a borrowed book by customer ID and book ID."""
    if library_system.return_book(customer_id, book_id):
        return {"message": "Book returned successfully"}
    raise HTTPException(
        status_code=404,
        detail="Book or customer not found or book is already available",
    )


@app.get("/books/", tags=["Books"])
def get_available_books():
    """Get all available books."""
    return library_system.get_available_books()


@app.get("/customers/", tags=["Customers"])
def get_customers():
    """Get all customers."""
    return library_system.get_customers()


@app.get("/customers/{customer_id}/borrowed/", tags=["Customers"])
def get_customer_borrowed_books(customer_id: int):
    """Get all books borrowed by a customer."""
    return library_system.get_customer_borrowed_books(customer_id)
