from os.path import exists

from_file = "from.txt"
to_file = "in.txt"

print(f"копирование данных из файла {from_file} в файл {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"Исходный файл имеет размер {len(indata)} байт")
print(f"Целевой файл существует? {exists(to_file)}")
print("Готов. Нажмите клавишу Enter для продолжения или ctrl+c для отмены.")
input(" > ")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Отлично. Все сделано")

out_file.close()
in_file.close()

