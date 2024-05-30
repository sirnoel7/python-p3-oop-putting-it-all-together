#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            if value > 0:
                self._page_count = value
            else:
                raise ValueError("page_count must be a positive integer")
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def get_book_info(self):
        return f"Title: {self.title}, Page Count: {self.page_count}"
