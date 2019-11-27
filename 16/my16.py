filename = input("Введите название файла. Если такого нет, то я создам новый ")

print("Открытие файла...")
target = open(filename, 'w')

print("Очистка файла.")
target.truncate()

print("Теперь я запрашиваю у Вас 3 строки")
line1 = input("Строка 1: ")
line2 = input("Строка 2: ")
line3 = input("Строка 3: ")

print("Это я запишу в файл.")
target.write("{}{}{}{}{}{}".format(line1, "\n", line2, "\n", line3, "\n"))

print("Закрытие файла.")
target.close()
