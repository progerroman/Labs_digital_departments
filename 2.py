import json


def task() -> float:
    # Открытие файла с данными и чтение их
    with open("input.json", "r") as file:
        data = json.load(file)  # Читаем содержимое JSON файла

    # Вычисление суммы произведений
    total_sum = sum(item["score"] * item["weight"] for item in data)

    # Округление результата до 3 знаков после запятой
    return round(total_sum, 3)


# Проверка функции
print(task())
