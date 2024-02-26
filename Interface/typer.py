import typer
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from controller.control import LibrarySystem

app = typer.Typer()
library_system = LibrarySystem


@app.command()
def add_book(title: str, author: str, genre: str):
    library_system.add_book(title, author, genre)
    typer.echo("Book added successfully!")


@app.command()
def delete_book(book_id: int):
    if library_system.delete_book(book_id):
        typer.echo("Book deleted successfully!")
    else:
        typer.echo("Failed to delete book. Please check the ID or try again later.")


@app.command()
def add_customer(name: str, email: str):
    library_system.add_customer(name, email)
    typer.echo("Customer added successfully!")


@app.command()
def delete_customer(cus_id: int):
    if library_system.delete_customer(cus_id):
        typer.echo("Customer deleted successfully!")
    else:
        typer.echo("Failed to delete customer. Please check the ID or try again later.")


@app.command()
def borrow_book(customer_id: int, book_id: int):
    if library_system.borrow_book(customer_id, book_id):
        typer.echo("Book borrowed successfully!")
    else:
        typer.echo("Failed to borrow book. Please check the IDs.")


@app.command()
def return_book(customer_id: int, book_id: int):
    if library_system.return_book(customer_id, book_id):
        typer.echo("Book returned successfully!")
    else:
        typer.echo("Failed to return book. Please check the IDs.")


@app.command()
def available_books():
    available_books = library_system.get_available_books()
    typer.echo("Available Books:")
    for book in available_books:
        typer.echo(
            f"ID: {book['_id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}"
        )


@app.command()
def borrowed_books():
    borrowed_books = library_system.get_borrowed_books()
    typer.echo("Borrowed Books:")
    for book in borrowed_books:
        typer.echo(
            f"ID: {book['_id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}"
        )


@app.command()
def customers():
    customers = library_system.get_customers()
    typer.echo("Customers:")
    for customer in customers:
        typer.echo(
            f"ID: {customer['_id']}, Name: {customer['name']}, Email: {customer['email']}"
        )


@app.command()
def customer_borrowed_books(customer_id: int):
    borrowed_books = library_system.get_customer_borrowed_books(customer_id)
    typer.echo("Books borrowed by the customer:")
    for book in borrowed_books:
        typer.echo(
            f"ID: {book['_id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}"
        )


if __name__ == "__main__":
    app()
