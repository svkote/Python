print("Практика и закрепление материала\nЯ уже знаю об управляюющих последовательностях с символом \\, "
      "которые:\n\nУправляют переносом строк\nи \t отступами.")

poem = """
\tДля счастья мне
Совсем немного надо.
Хочу тебя я \nнежно обнимать.
Хочу всегда
я быть с тобою рядом
\n\t\tи никогда не отпускать!
"""

print("-" * 20, poem, "-" * 20)

five = 10 - 2 + 3 - 6
print(f"Здесь должна быть пятерка: {five}")


def secret_formula(started):
    return started * 500, started * 500 / 1000, started * 500 / 1000 / 100


start_point = 10000
beans, jars, crates = secret_formula(start_point)
print("Начиная с: {}".format(start_point))
print(f"У нас есть {beans} бобов, {jars} банок, {crates} ящиков.")

start_point = start_point / 10
formula = secret_formula(start_point)
print("У нас есть {} бобов, {} банок, {} ящиков.".format(*formula))
