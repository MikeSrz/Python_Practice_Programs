import functools

class Song:
    def __init__(self, title="Sin Catalogar", author="Sin Catalogar"):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if not isinstance(other, Song):
            return NotImplemented
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.author < other.author

    """
    def sort_by_author(self, other):
        if not isinstance(other, Song):
            return NotImplemented
        return 
    """
    def __str__(self):
        return f"Título: {self.title}, Autor: {self.author}"
