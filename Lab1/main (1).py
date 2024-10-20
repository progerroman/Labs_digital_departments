numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Найдём сумму всех элементов, исключая None
sum_of_numbers = 0
for i in range(len(numbers)):
    if numbers[i] != None:
        sum_of_numbers += numbers[i]

# Вычисляем количество элементов списка (включая пропущенный элемент)
n = len(numbers)

# Вычисляем среднее арифметическое
average = sum_of_numbers / n

# Заменим пропущенный элемент на среднее арифметическое
numbers[numbers.index(None)] = average

print("Измененный список:", numbers)

