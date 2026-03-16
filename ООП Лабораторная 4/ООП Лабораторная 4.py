class Transport:
    """Базовый класс, Транспортное средство"""
    def __init__(self, speed: int, color: str):
        """ Инициализация Т.с."""
        self._speed = speed
        self._color = color

    def get_speed(self) -> int:
        """Возвращает скорость т.с."""
        return self._speed

    def get_color(self) -> str:
        """Возвращает цвет т.с."""
        return self._color

    def move(self) -> str:
        """Возвращает описание движения т.с."""
        return f'Транспорт движется со скоростью {self._speed} км/ч'

    def __str__(self) -> str:
        """Возвращает читаемый текст для пользователя"""
        return f'Транспорт {self._color} цвета, скорость {self._speed} км/ч'

    def __repr__(self) -> str:
        """Возвращает читаемый текст для разработчика"""
        return f'Transport: speed={self._speed}, color={self._color!r}'


class Motocycle(Transport):
    """Дочерний класс транспорта - мотоцикл"""
    def __init__(self, speed: int, color: str, brand: str):
        """Расширение базового класса с помощью марки мотоцикла"""
        super().__init__(speed, color)
        self._brand = brand

    def get_brand(self) -> str:
        """ Возвращает марку мотоцикла"""
        return self._brand

    def move(self) -> str:
        """Перегружение метода. Возвращает описание движения мотоцикла"""
        return f'{self._brand} {self._color} цвета движется со скоростью {self._speed} км/ч'

    def time_to_point(self, distance: float) -> float:
        """ Возвращает время, необходимое для преодоления расстояния до точки"""
        return distance / self._speed

    def __str__(self) -> str:
        """Перегружение магического метода.Возвращает читаемый текст для пользователя """
        return f'{self._brand} {self._color} цвета, скорость {self._speed} км/ч'

    def __repr__(self) -> str:
        """Перегружение магического метода.Возвращает читаемый текст для разработчика """
        return f'Car: speed={self._speed!r}, color={self._color!r}, brand={self._brand}'


if __name__ == "__main__":
    transport = Transport(50, "синего")
    motocycle = Motocycle(150, "розового", "Yamaha")

    print("Транспорт:")
    print(transport)
    print(transport.move())
    print(repr(transport))

    print("Мотоцикл:")
    print(motocycle)
    print(motocycle.move())
    r_distance = 100
    time = motocycle.time_to_point(r_distance)
    print(f'До точки осталось {time: .1f} ч.')
    print(repr(motocycle))
    pass