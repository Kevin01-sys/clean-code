import os
from datetime import datetime

from Page import Page


class Book:
    BOOK_DIRECTORY_PATH = os.path.join(os.getcwd(), "tmp")

    def __init__(self, title: str, author: str, pages: list['Page']):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = self.pages[0]

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_current_page(self):
        return self.current_page

    def turn_page(self):
        next_page_index = self.current_page.number
        if next_page_index < len(self.pages):
            self.current_page = self.pages[next_page_index]

    def turn_page_back(self):
        previous_page_index = self.current_page.number - 2
        if previous_page_index >= 0:
            self.current_page = self.pages[previous_page_index]

    def save(self):
        try:
            book_file_path = os.path.join(Book.BOOK_DIRECTORY_PATH, f"{self.title}_{datetime.now().timestamp()}.txt")
            with open(book_file_path, "w") as writer:
                for page in self.pages:
                    writer.write(f"---- Page {page.number} ----\n")
                    writer.write(f"{page.content}\n")
        except IOError as e:
            print(f"Error al guardar el libro: {e}")