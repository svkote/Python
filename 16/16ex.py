# close - закрывает файл
# read - считывает содержимое файла
# readline - считывает только одну строку из текстового файла
# truncate - очищает файл
# write - записывает данные в файл
# seek(0) - перемещает указатель текущей позиции чтения/записи в начало файла

from sys import argv

script, filename = argv

print(f"Я собираюсь стереть файл {filename}")
print("Если Вы не собираетесь его стирать - нажмите сочетание клавиш ctrl + C")
print("Если хотите стереть файл - нажмите Enter")
input("?")

print("Открытие файла..")
target = open(filename, 'w')

print("Очистка файла.")
target.truncate()

print("Теперь я запрашиваю у Вас 3 строки")
line1 = input("Строка 1: ")
line2 = input("Строка 2: ")
line3 = input("Строка 3: ")

print("Это я запишу в файл.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Закрытие файла.")
target.close()
