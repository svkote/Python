name = input("Как твое имя?\n")
print(f"""
Это логическая квест-игра по сбору ключей в старом заброшенном здании. Сможешь собрать их все, {name}?
Всего в здании 3 комнаты. Заходить в каждую из них можно лишь 2 раза.
В каждой комнате тебя ждет небольшое испытание.
""")

keys = 0
room_1 = 2
room_2 = 2
room_3 = 2


def hall(number_of_keys, number_of_attempts_room_1, number_of_attempts_room_2, number_of_attempts_room_3):
    print(f""" 
    Ты находишься в прихожей. Перед тобой 3 комнаты. Какую ты выберешь?
    1 - Кухня. Ты можешь зайти сюда еще {number_of_attempts_room_1} раз.
    2 - Спальня. Ты можешь зайти сюда еще {number_of_attempts_room_2} раз.
    3 - Гостинная. Ты можешь зайти сюда еще {number_of_attempts_room_3} раз.
    Количество ключей: {number_of_keys}""")
    choice = input(" >> \n")
    if choice == "1":
        if number_of_attempts_room_1 <= 0:
            print("Ты безуспешно дергаешь ручку, но, к сожалению, все твои попытки туда зайти исчерпаны."
                  "Попробуй выбрать другую комнату")
            hall(number_of_keys, number_of_attempts_room_1, number_of_attempts_room_2, number_of_attempts_room_3)
        else:
            room1(number_of_keys, number_of_attempts_room_1 - 1, number_of_attempts_room_2, number_of_attempts_room_3)


def room1(number_of_keys, number_of_attempts_room_1, number_of_attempts_room_2, number_of_attempts_room_3):
    keys_in_room1 = number_of_keys
    if number_of_attempts_room_1 > 2:
        step1 = input(f"""Ты находишься на кухне. 
        Внезапно перед тобой возникает кухарка с ножом в руках.Что ты будешь делать?
        1. Попытаюсь отобрать нож.
        2. Выйду-ка я лучше из комнаты от греха подальше.\n\n""")
        if step1 == "1":
            print("""Кухарка оказалась слабым противником и ты случайно ее зарезал. 
            В кармане ее фартука ты находишь первый ключ. И... вдруг тебя охватывает паника и ты выбегаешь""")
            keys_in_room1 += 1
            hall(keys_in_room1, number_of_attempts_room_1, number_of_attempts_room_2, number_of_attempts_room_3)
        if step1 == "2":
            print("Ты коришь себя за эту ошибку, так как, возможно, это была твоя попытка забрать ключ.")
            hall(keys_in_room1, number_of_attempts_room_1, number_of_attempts_room_2, number_of_attempts_room_3)


start = input(f"Ты готов, {name}? Введи 1.\n\n")
if start == "1":
    print("Ну тогда приступим!")
    hall(keys, room_1, room_2, room_3)
