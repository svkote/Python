#-*- coding: UTF-8 -*-
from sys import argv

# передаем в консоли значения для переменной filename
script, filename = argv

# присваиваем переменной txt действие открыть файл filename
txt = open(filename)


print(f"Содержимое файла: {filename}")
# Выводим содержимое файла в консоль
print(txt.read())

print("Снова введите имя файла: ")
file_again = input(" >> ")

txt_again = open(file_again)

print(txt_again.read())
