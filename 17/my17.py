from os.path import exists

from_file = "from.txt"
to_file = "in.txt"
indata = open(from_file).read()

input(f"""Копирование данных из файла {from_file} в файл {to_file}.\n Исходный файл имеет размер {len(indata)} байт. \nЦелевой файл существует? {exists(to_file)}\nГотов. \nНажмите клавишу Enter для продолжения или ctrl+c для отмены.> """)

open(to_file, 'w').write(indata)
print("Отлично. Все сделано")

open(to_file, 'w').close()
open(from_file).close()

