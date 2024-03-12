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

    def get_title(self) -> str:
        return self.title

    def get_author(self) -> str:
        return self.author

    def get_current_page(self) -> Page:
        return self.current_page

    def get_pages(self) -> list['Page']:
        return self.pages

    def turn_page(self) -> None:
        next_page_index = self.current_page.number
        if next_page_index < len(self.pages):
            self.current_page = self.pages[next_page_index]

    def turn_page_back(self) -> None:
        previous_page_index = self.current_page.number - 2
        if previous_page_index >= 0:
            self.current_page = self.pages[previous_page_index]