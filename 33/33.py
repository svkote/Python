numbers = []


def loop(number, b=0):
    while b != number:
        print(f"В начале значение b равно {b}")
        numbers.append(b)
        b += 1
        print("Текущие значения: ", numbers, f"\nВ конце значение b равно {b}")
    print("Значения: ", end="")
    for num in numbers:
        print(num, end=", ")


loop(6)
