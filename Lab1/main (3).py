# TODO Найдите количество книг, которое можно разместить на дискете

# Данные задачи
disk_size_mb = 1.44  # Объем дискеты в Мб
pages_per_book = 100  # Количество страниц в книге
lines_per_page = 50   # Количество строк на странице
chars_per_line = 25   # Количество символов в строке
bytes_per_char = 4    # Объем одного символа в байтах

# Шаги расчета
disk_size_bytes = disk_size_mb * 1024 * 1024  # Объем дискеты в байтах
chars_per_book = pages_per_book * lines_per_page * chars_per_line  # Количество символов в книге
book_size_bytes = chars_per_book * bytes_per_char  # Объем книги в байтах

# Количество книг, помещающихся на дискету
books_on_disk = disk_size_bytes // book_size_bytes  # Целое число книг

print("Количество книг, помещающихся на дискету:", int(books_on_disk))
