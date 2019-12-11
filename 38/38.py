ten_things = "Яблоки Апельсины Вороны Телефоны Свет Сахар"
stuff = ten_things.split(' ')
more_stuff = ["День", "Ночь", "Песня", "Мишка", "Кукуруза", "Банан", "Девочка", "Мальчик"]
while len(stuff) != 13:
    next_one = more_stuff.pop(0)
    print("Добавляем ", next_one)
    stuff.append(next_one)
    print(f"Теперь у нас {len(stuff)} обьектов")

print("Итак: ", stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(', '.join(stuff))
print('#'.join(stuff[3:5]))
