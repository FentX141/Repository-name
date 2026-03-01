class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        """Геттер для названия книги (только для чтения)"""
        return self._name

    @property
    def author(self):
        """Геттер для автора книги (только для чтения)"""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажной книги, наследующийся от Book"""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # используем сеттер для проверки

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Класс для аудиокниги, наследующийся от Book"""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # используем сеттер для проверки

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float(value)

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


# Пример использования
if __name__ == "__main__":
    # Создаем экземпляры книг
    paper_book = PaperBook("Бойцовкий клуб", "Чак Паланик", 256)
    audio_book = AudioBook("Десять нигритят", "Агата Кристи", 7.2)

    # Проверяем методы
    print(paper_book)
    print(audio_book)
    print(repr(paper_book))
    print(repr(audio_book))

    # Проверяем неизменяемость name и author
    # paper_book.name = "Новое название"  # Ошибка! AttributeError

    # Проверяем валидацию
    try:
        paper_book.pages = -100  # Ошибка! ValueError
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        audio_book.duration = "два часа"  # Ошибка! TypeError
    except TypeError as e:
        print(f"Ошибка: {e}")