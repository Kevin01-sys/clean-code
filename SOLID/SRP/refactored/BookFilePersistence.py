import os
from Book import Book
from i_book_persistence import IBookPersistence
from datetime import datetime
from BookPersistenceException import BookPersistenceException


class BookFilePersistence(IBookPersistence):

    @staticmethod
    def save(book: Book) -> None:
        book_file_path = os.path.join(Book.BOOK_DIRECTORY_PATH, f"{book.title}_{datetime.now().timestamp()}.txt")
        pages = book.get_pages()

        try:
            with open(book_file_path, "w") as writer:
                for page in pages:
                    writer.write(f"---- Page {page.number} ----\n")
                    writer.write(f"{page.content}\n")
        except Exception as e:
            raise BookPersistenceException("Error al guardar el libro en el archivo: " + str(e))
