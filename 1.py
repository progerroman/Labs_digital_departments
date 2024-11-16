import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Чтение данных из CSV файла
    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)  # Используем DictReader для автоматического преобразования строк в словари
        data = [row for row in csv_reader]  # Преобразуем строки в список словарей

    # Запись данных в JSON файл с отступами
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)  # Отступы равны 4, поддержка unicode символов

if __name__ == '__main__':
    # Выполняем задачу
    task()

    # Для проверки выводим содержимое созданного JSON файла
    with open(OUTPUT_FILENAME, mode='r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
