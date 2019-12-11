# Yield — это ключевое слово которое используется так же, как и слово return. Разница в том, что функция при этом
# начинает возвращать генератор вместо значения.


def create_generator():
    my_list = range(3)
    for i in my_list:
        yield i * i


my_generator = create_generator()  # создаём генератор
print(my_generator)  # my_generator является объектом!
for i in my_generator:
    print(i)
