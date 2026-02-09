from typing import Union
import doctest
# TODO Написать 3 класса с документацией и аннотацией типов

class Car:
    def __init__(self, gasoline: int, speed: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param gasoline: Количество литров бензина в баке от 0 до 50
        :param speed: Скорость автомобиля

        Примеры:
        car = Car(40, 110)  # инициализация экземпляра класса
        """
        if not isinstance(gasoline, int):
            raise TypeError("Количество литров бензина должно быть типа int")
        if gasoline < 0 or gasoline > 50:
            raise ValueError("Количество литров бензина должно быть числом от 0 до 50")
        self.gasoline = gasoline


        if not isinstance(speed, float):
            raise TypeError("Скорость автомобиля должна быть типа float")
        if not speed > 0:
            raise ValueError("Скорость автомобиля должна быть положительным числом")
        self.speed = speed

    def change_gasoline(self, change_v: int) -> None:
        """
        Изменение количества литров бензина.
        :param change_v: изменение количества литров бензина

        :raise ValueError: Если новое количество литров бензина не является числом от 0 до 50

        Примеры:
        car = Car(34, 155)
        car.change_gasoline(-20)
        """
        if not isinstance(change_v, int):
            raise TypeError("Изменение количества литров бензина должно быть типа int")
        if self.gasoline + change_v < 0 or self.gasoline + change_v > 50:
            raise ValueError("Новое количество литров бензина должна быть числом от 0 до 50")
        ...
    def change_speed(self, new_speed: float) -> None:
        """
        Изменение скорости автомобиля.
        :param new_speed: Новая скорость автомобиля

        :raise ValueError: Если новая скорость автомобиля не является целым числом
        Примеры:
        car = Car(15, 52)
        car.change_speed(5)
        """
        if not isinstance(new_speed, float):
            raise TypeError("Новая скорость автомобиля должна быть типа float")
        if not new_speed > 0:
            raise ValueError("Новая скорость автомобиля должна быть положительным числом")
        ...

class Electric_guitar:
    def __init__(self, volume: int, is_on: bool):
        """
        Создание и подготовка к работе объекта "Электрогитара"

        :param volume: Уровень громокости от 0 до 100
        :param is_on: Включена ли электрогитара к аудиокарте
        Примеры:
         electric_guitar = Electric_guitar(69, True)  # инициализация экземпляра класса
        """
        if not isinstance(volume, int):
            raise TypeError("Уровень громкости должен быть типа int")
        if volume < 0 or volume > 100:
            raise ValueError("Уровень громкости должен быть числом от 0 до 100")
        self.volume = volume

        if not isinstance(is_on, bool):
            raise TypeError("Включена ли электрогитара к аудиокарте должно быть тип bool")
        self.is_on = is_on

    def charge(self, percentage: int) -> None:
        """
        Увеличение громкости на даноое количество процентов
        :param percentage: Изменение уровня громкости

        :raise ValueError: Если новый уровень громкости не является числом от 0 до 100

        :raise ValueError: Если изменение уровня громкости не является положительным числом
        Примеры:
         electric_guitar = Electric_guitar(33, False)
         electric_guitar.charge(25)
        """
        if not isinstance(percentage, int):
            raise TypeError("Изменение уровня громкости должно быть типа int")
        if self.volume + percentage < 0 or self.volume + percentage > 100:
            raise ValueError("Новый уровень громкости должен быть числом от 0 до 100")
        if not percentage > 0:
            raise ValueError("Изменение уровня громкости должно быть положительным числом")
        ...

class Music_player:
    def __init__(self, artist: str, song: str):
        """
        Создание и подготовка к работе объекта "Музыкальный проигрыватель"

        :param artist: Текущий исполнитель
        :param song: Текущая песня
        Примеры:
        music_player = Music_player("Nirvana", "Smells Like Teen Spirit")  # инициализация экземпляра класса
        """
        if not isinstance(artist, str):
            raise TypeError("Текущий исполнитель должен быть типа str")
        self.artist = artist

        if not isinstance(song, str):
            raise TypeError("Текущая песня должна быть типа str")
        self.song = song
        ...

    def change_song(self, new_artist: str, new_song: str) -> None:
        """
        Смена песни в наушниках
        :param new_artist: Новый исполнитель

        :param new_song: Новая песня

        Примеры:
        music_player = Music_player("Djo", "End of Beginning")  # инициализация экземпляра класса
        music_player.change_song("Lil Uzi Vert", "It's A Dream")
        """
        if not isinstance(new_artist, str):
            raise TypeError("Новый исполнитель должен быть типа str")
        if not isinstance(new_song, str):
            raise TypeError("Новая песня должна быть типа str")
        ...

if __name__ == "__main__":
    doctest.testmod()# TODO работоспособность экземпляров класса проверить с помощью doctest