import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Programmer:
    def __init__(self,experience:int, age:int, count_of_projects:int):
        if (not isinstance(experience, int)) or (not isinstance(age, int)) or (not isinstance(count_of_projects, int)):
            raise TypeError("Error Type: Class programmer")
        if (experience < 0) or (age <= 0) or (count_of_projects < 0):
            raise ValueError("Error Value: Class programmer")
        self.exp = experience
        self.age = age
        self.cnt = count_of_projects
    """
    Создание и подготовка к работе объекта "Программист"
    :param experience: Опыт работы(некоторый показатель)
    :param age: Биологический возраст
    :count_of_projects: Количество успешно завершённых рабочих проектов
    
    Примеры:
    >>> programmer = Programmer(13, 22, 3) # Инициализация экземпляра класса
    """
    def raise_exp(self, count: int) -> None:
        """
        Функция повышения опыта
        :param count: Коэффициент для увеличения опытп
        :return: None

        Примеры:
        >>> programmer = Programmer(13, 22, 3)
        >>> programmer.raise_exp(10)
        """
        if not isinstance(count ,int):
            raise TypeError("Error Type: Class programmer, Type experience")
        if count < 0:
            raise ValueError("Error Value: Class programmer, Value count")
        self.exp += count
    def check_out_successful_projects(self, count_of_projects:int, succeed: bool) -> bool:
        """
        Проверка успешности реализованного проекта
        :param succeed: Флаг проверки
        :return: Результат проверки

        Примеры:
        >>> programmer = Programmer(13, 22, 3)
        >>> programmer.check_out_successful_projects(3, True)
        True
        """
        if not isinstance(succeed, bool):
            raise TypeError("Error Type: Class programmer,Type succeed")
        return succeed
class Student:
    def __init__(self, course: int, count_of_retakes: int, average_mark: float):
        """
        Создание и подготовка к работе объекта "Студент"
        :param course: Курс обучения в университете
        :param count_of_retakes: Количество пересдач(довольно больная тема)
        :param average_mark: Средний балл обучения

        Примеры:
        >>> student = Student(3, 5, 4.35)
        """
        if (not isinstance(course, int)) or (not isinstance(count_of_retakes, int) or not isinstance(average_mark, float)):
            raise TypeError("Error Type: Class student")
        if (course <= 0) or (count_of_retakes < 0) or (average_mark < 2):
            raise ValueError("Error Value: Class student")
        self.course = course
        self.cnt = count_of_retakes
        self.average_mark = average_mark
    def end_university(self) -> None:
        """
        Функция проверки пора ли окончить университет

        :return: None

        Примеры:
        >>> student = Student(5, 5, 4.35)
        >>> student.end_university()
        Congratulations! :)
        >>> student = Student(3, 2, 3.7)
        >>> student.end_university()
        """
        if (self.course > 4):
            print("Congratulations! :)")
    def red_diploma(self) -> bool:
        """
        Функция проверки требований для получения красного диплома

        :return: Результат проверки

        Примеры:
       >>> student = Student(3, 5, 4.35)
        >>> student.red_diploma()
        False
        >>> student = Student(3, 5, 4.8)
        >>> student.red_diploma()
        True
        """
        return self.average_mark >= 4.7
class Site:
    def __init__(self, users: int, rating: int):
        """
        Создание и подготовка к работе объекта "Сайт"

        :param users: Количество ежедневных пользователей
        :param rating: Рейтинг сайта по 10-балльной шкале

        Примеры:
        >>> site = Site(120, 6)
        """
        if not isinstance(users, int):
            raise TypeError("Error Type: Class site")
        if not isinstance(rating, int):
            raise TypeError("Error Type: Class site")
        if(users < 0):
            raise ValueError("Error Value: Class site")
        if not (1 <= rating <= 10):
            raise ValueError("Error Value: Class site")
        self.users = users
        self.rating = rating
    def add_advertisments(self, ads: int) -> int:
        """
        Размещение рекламы на сайте в зависимости от количества пользователй

        :param ads: Количество рекламы

        Примеры:
        >>> site = Site(120, 6)
        >>> site.add_advertisments(120)
        """
        if not isinstance(ads, int):
            raise TypeError("Error Type: Class site")
        if ads <= 0:
            raise ValueError("Error Value: Class site, Value ads")
        pass
    def earnings_from_the_site(self) -> float:
        """
        Вычисление ежемесячного заработка с сайта

        :return: Доход
        """
        return self.users * self.rating * 0.36

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
