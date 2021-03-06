print("""
Это логическая квест-игра по сбору ключей в старом заброшенном здании. Сможешь собрать их все?
Всего в здании 3 комнаты. Заходить в каждую из них можно лишь 1 раз.
В каждой комнате тебя ждет небольшое испытание.
""")


def hall(number_of_attempts_room_1, number_of_attempts_room_2, number_of_attempts_room_3):
    print(f""" 
    Ты находишься в прихожей. Перед тобой 3 комнаты. Какую ты выберешь?
    1 - Кухня. Ты можешь зайти сюда {number_of_attempts_room_1} раз.
    2 - Спальня. Ты можешь зайти сюда {number_of_attempts_room_2} раз.
    3 - Гостинная. Ты можешь зайти сюда {number_of_attempts_room_3} раз.""")
    return input(" >> \n")


def room1():
    step = input(f"""
    Ты находишься на кухне. 
    Внезапно перед тобой возникает кухарка с ножом в руках.Что ты будешь делать?
    1. Попытаюсь отобрать нож.
    2. Попробую узнать который час\n\n""")
    if step == "1":
        print("""
        Кухарка оказалась слабым противником и ты случайно ее зарезал. 
        В кармане ее фартука ты находишь первый ключ. И... вдруг тебя охватывает паника и ты выбегаешь""")
        return 1
    elif step == "2":
        print("\tОтветив, она тут же вышла из комнаты. Обыскав все шкафы ты выходишь оттуда ни с чем..")
        return 0
    else:
        print("Неверный ввод, попробуй снова!")
        room1()


def room2():
    step = input(f"""
    Ты в спальне. Вокруг абсолютная тьма. Ты безуспешно пытаешься найти выключатель.
    И вдруг ты слышишь чье-то тяжелое дыхание. Твои действия?
    1. Попробую призвать на помощь Ктулху.
    2. Попробую насвистеть 'Черный ворон'
    3. Постараюсь не дышать и подождать когда этот кто-то уйдет\n\n""")
    if step == "1":
        print("""
        Пока ты пытался призвать мысленно Ктулху этот кто-то ушел.
        Ты нашел в своем кармане зажигалку и после недолгих поисков вышел из комнаты с ключом""")
        return 1
    elif step == "2":
        print("\tБезумие охватило тебя и ты выбежал из комнаты прочь.")
        return 0
    elif step == "3":
        print("""
        Ты просидел там около часа и наконец услышал мирный храп.
        Ты нашел в своем кармане зажигалку и после недолгих поисков вышел из комнаты с ключом""")
        return 1
    else:
        print("\tНеверный ввод, попробуй снова!")
        room2()


def room3():
    step = input(f"""
    Ты находишься в гостинной. 
    Внезапно перед тобой возникает огромный злой доберман.
    1. Попробую отыскать в кармане косточку или мячик.
    2. Заору собаке в ухо\n\n""")
    if step == "1":
        print("""
        Конечно же косточки нет и ты в страхе пятишься назад от собаки. 
        Тебя охватывает паника и ты выбегаешь""")
        return 0
    elif step == "2":
        print("""
        Так как в детстве тебе наступил на ухо медведь - собака в приступе ужаса выбежала из комнаты.
        Ты спокойно обыскал всю комнату и нашел ключ.""")
        return 1
    else:
        print("\tНеверный ввод, попробуй снова!")
        room3()


keys = 0
room_1 = 1
room_2 = 1
room_3 = 1
attempt = 4

start = input(f"Ты готов? Введи 1.\n\n")
if start == "1":
    print("Ну тогда приступим!")
    while attempt > 1:
        attempt -= 1
        print(f"Количество попыток: {attempt}. Количество ключей: {keys}")
        selection = hall(room_1, room_2, room_3)
        if selection == "1":
            if room_1 != 0:
                room_1 -= 1
                keys += room1()
            elif room_1 == 0:
                print("Ты больше не можешь сюда войти!")
                attempt += 1
        elif selection == "2":
            if room_2 != 0:
                room_2 -= 1
                keys += room2()
            elif room_2 == 0:
                print("Ты больше не можешь сюда войти!")
                attempt += 1
        elif selection == "3":
            if room_3 != 0:
                room_3 -= 1
                keys += room3()
            elif room_3 == 0:
                print("Ты больше не можешь сюда войти!")
                attempt += 1
        else:
            print("Неверный ввод, попробуй снова!")
            attempt += 1
    print(f"""
    Ты заработал {keys} ключа из 3 возможных!
    Все попытки закончились""")
else:
    print("Нет так нет!")
