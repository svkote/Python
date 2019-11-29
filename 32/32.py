the_count = [1, 2, 3, 4, 5]
fruits = ['яблоко', 'апельсин', 'персик', 'абрикос']
change = [1, 'червонец', 'полтинник', 3, 'сотню', 5]

for number in the_count:
    print(f"Счетчик: {number}")

for fruit in fruits:
    print(f"Фрукт: {fruit}")

for i in change:
    print(f"Получено: {i}")

elements = []

for i in range(0, 10):
    print(f"Добавление в список: {i}")
    elements.append(i)


for i in elements:
    print(f"Номер элемента: {i}")

print(elements)
