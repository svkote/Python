# from sys import argv
#
# script, input_file = argv
input_file = "test.txt"


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline(), end=" ")


current_file = open(input_file)

print("Первым делом выведем этот файл целиком: \n")
print_all(current_file)

print("Теперь отмотаем назад, словно это кассета.")
rewind(current_file)

print("Выведем три строки:")
for i in range(1, 4):
    print_a_line(i, current_file)
