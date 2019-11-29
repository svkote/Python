numbers = []


def loop(number):
    b = 0
    while b != number:
        print(f"В начале значение b равно {b}")
        numbers.append(b)
        b += 1
        print("Текущие значения: ", numbers)
        print(f"В конце значение b равно {b}")


loop(6)

print("Значения: ")

for num in numbers:
    print(num)
