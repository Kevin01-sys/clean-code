from Page import Page
from Book import Book
from BookFilePersistence import BookFilePersistence
from BookPersistenceException import BookPersistenceException


def main():
    pages = [Page(1, "Contenido de la página 1"),
             Page(2, "Contenido de la página 2"),
             Page(3, "Contenido de la página 3")]

    book: Book = Book("Título del libro", "Autor del libro", pages)

    try:
        BookFilePersistence.save(book)
    except BookPersistenceException as e:
        print("Ocurrió un error de persistencia de libros:", e)


if __name__ == "__main__":
    main()