name = "Зед Шоу"
age = 35
height = 188
weight = 80
eyes = "голубые"
teeth = "белые"
hair = "каштановые"

print(f"Давайте поговрим о человеке по имени {name}.")
print(f"Его рост составляет {height} см.")
print(f"Он весит {weight} кг.")
print(f"У него {eyes} глаза и {hair} волосы.")
print(f"Его зубы обычно {teeth}, хотя он и любит пить кофе.")

total = age + height + weight
print(f"Если сложить {age}, {height} и {weight}, то получится {total}")

# перевод см в метры

sm = 200
# meter = sm/100
print(f"Переведем {sm} см в метры. Получится: {round(sm/100)} м")


# перевод киллограммы в тонны

kg = 5000
print(f"Переведем {kg} кг в тонны. Получится: {round(kg/1000)} тонн")
