class Auto:
    """
    Базовый класс для представления автомобиля.

    Атрибуты:
        _counts_of_wheels (int): Количество колес у автомобиля.
        Количество колес после выхода с завода нельзя менять, поэтому инкапсуляция
        weight (float): Вес автомобиля в тоннах.
        color (str): Цвет автомобиля.

    Методы:
        speed() -> float: Рассчитывает скорость автомобиля.
        description() -> str: Возвращает строковое описание автомобиля.
        check_main() -> None: Проверяет корректность переданных атрибутов.
        __str__() -> str: Возвращает строковое представление объекта.
        __repr__() -> str: Возвращает строковое представление объекта для отладки.
    """

    def __init__(self, wheels: int, weight: float, color: str) -> None:
        """
        Инициализирует объект класса Auto.

        Параметры:
            wheels (int): Количество колес.
            weight (float): Вес автомобиля.
            color (str): Цвет автомобиля.
        """
        self._counts_of_wheels = wheels
        self.weight = weight
        self.color = color
        self.check_main()

    def speed(self) -> float:
        """
        Рассчитывает скорость автомобиля по формуле.

        Возвращает:
            float: Значение скорости.
        """
        return 23.7 + self._counts_of_wheels * 0.05 - self.weight*0.72

    def description(self) -> str:
        """
        Возвращает описание автомобиля с указанием цвета, количества колес и веса.
        В дочернем классе он у нас будет просто наследоваться

        Возвращает:
            str: Описание автомобиля.
        """
        return f"{self.color} auto with {self._counts_of_wheels} wheels and weight {self.weight} tons."

    def check_main(self) -> None:
        """
        Проверяет корректность значений атрибутов.
        """
        if self._counts_of_wheels < 0:
            raise ValueError("Value error with 'counts_of_wheels'")
        if not isinstance(self._counts_of_wheels, int):
            raise TypeError("Type error with 'counts_of_wheels'")
        if not isinstance(self.weight, float):
            raise TypeError("Type error with 'weight'")
        if self.weight < 0:
            raise ValueError("Value error with 'weight'")
        if not isinstance(self.color, str):
            raise TypeError("Type error with 'color'")

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Возвращает:
            str: Строка с основными атрибутами объекта.
        """
        return f"{self._counts_of_wheels}, {self.weight}, {self.color}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки.

        Возвращает:
            str: Строка, содержащая информацию об объекте.
        """
        return f"Auto(counts_of_wheels='{self._counts_of_wheels}', weight='{self.weight}', color='{self.color}')"


class BMW(Auto):
    """
    Дочерний класс, представляющий автомобили BMW.

    Атрибуты:
        name (str): Название модели BMW.
        is_sportcar (bool): Флаг, указывающий, является ли автомобиль спортивным.

    Методы:
        speed() -> float: Перегруженный метод расчета скорости.
        check_child() -> None: Проверка атрибута name.
    """

    def __init__(self, wheels: int, weight: float, name: str, is_sportcar_flag: bool, color: str) -> None:
        """
        Инициализирует объект класса BMW.

        Параметры:
            wheels (int): Количество колес.
            weight (float): Вес автомобиля.
            name (str): Название модели BMW.
            is_sportcar_flag (bool): Является ли автомобиль спортивным.
            color (str): Цвет автомобиля.
        """
        super().__init__(wheels, weight, color)
        self.name = name
        self.is_sportcar = is_sportcar_flag
        self.check_child()

    def speed(self) -> float:
        """
        Перегруженная версия метода speed.

        В спортивных моделях BMW коэффициент скорости выше, поэтому перегрузили.

        Возвращает:
            float: Значение скорости.
        """
        if self.is_sportcar:
            return 23.7 + self._counts_of_wheels * 0.85 - self.weight*0.72
        return super().speed()

    def check_child(self) -> None:
        """
        Добавляет проверку имени.
        """
        super().check_main()
        if not isinstance(self.name, str):
            raise TypeError("Type error with 'name'")

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта BMW.

        Возвращает:
            str: Строка с основными атрибутами объекта.
        """
        return f"{self.name}, {self._counts_of_wheels}, {self.weight}, {self.is_sportcar}, {self.color}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки.

        Возвращает:
            str: Строка, содержащая информацию об объекте.
        """
        return f"BMW(name='{self.name}', counts_of_wheels='{self._counts_of_wheels}', weight='{self.weight}', is_sportcar='{self.is_sportcar}', color='{self.color}')"


if __name__ == "__main__":
    bmw_x5 = BMW(4, 2.31, "X5", False, "black")
    bmw_i8 = BMW(4, 1.8, "i8", True, "white-blue")
    print(bmw_x5)
    print(bmw_i8)
    print(repr(bmw_x5))
    print(str(bmw_i8))
    print(bmw_i8.speed())
    print(bmw_x5.speed())
    if bmw_i8.speed() > bmw_x5.speed():
        print("i8 faster than x5. Maybe... I don't know. This is just example :D")