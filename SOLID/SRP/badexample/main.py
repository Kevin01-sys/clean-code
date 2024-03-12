from Page import Page
from Book import Book


def main():
    pages = [Page(1, "Contenido de la página 1"),
             Page(2, "Contenido de la página 2"),
             Page(3, "Contenido de la página 3")]

    book = Book("Título del libro", "Autor del libro", pages)
    book.save()


if __name__ == "__main__":
    main()