from sys import exit


def dead(why):
    print("Ты проиграл!", why)
    exit(0)


def start():
    """Стартовая позиция, появляется единожды"""
    print("""
    Ты очнулся в еле освещенной комнате на полу. Вокруг ободранные обои и в целом вся комната выглядит довольно жутко.
    Откуда-то слышаться пугающие звуки.
    Надо скорее выбираться из этого дома!
    Отсюда ведут две двери, налево(1) и направо(2).
    Куда ты повернешь?""")
    choice = input("> ")
    if choice == "1":
        dog_room()
    elif choice == "2":
        wardrobe_room()
    else:
        dead("Ты ходишь из стороны в сторону, и вскоре умираешь с голода.")


def start_room():
    """Стартовая позиция. Появляется при возвращении из 2 и 4 комнаты"""
    print("""
    Ты находишься в комнате в которой очнулся.
    Отсюда ведут две двери, налево(1) и направо(2).
    Куда ты повернешь?""")
    choice = input("> ")
    if choice == "1":
        dog_room()
    elif choice == "2":
        wardrobe_room()
    else:
        dead("Ты ходишь из стороны в сторону, и вскоре умираешь с голода.")


def dog_room():
    """Комната с доберманом"""
    print("""
    Ты заходишь в комнату и вдруг слышишь нарастающее рычание собаки.
    Перед тобой стоит доберман, готовый вот-вот тебя разорвать на куски.
    Ты пытаешься найти у себя хоть какое-то средство защиты, но все безуспешно.
    Что будешь делать?
    Можно вернуться назад(1), попробовать сразиться с собакой без оружия и пройти в дверь прямо(2) или направо(3)?
    """)
    choice = input("> ")
    if choice == "1":
        print("Ты в ужасе устремляешься назад и захлопываешь за собой дверь.")
        start_room()
    elif choice == "3":
        print("Ты вступаешь в схватку с собакой и в какой то момент у тебя получилось ее откинуть. Воспользовавшись "
              "моментом - ты убегаешь за дверь")
        insect_room()
    elif choice == "2":
        print("Ты вступаешь в схватку с собакой и в какой то момент у тебя получилось ее откинуть. Воспользовавшись "
              "моментом - ты убегаешь за дверь")
        acid_room()
    else:
        dead("Ты ходишь из стороны в сторону, и вскоре умираешь с голода.")


def wardrobe_room():
    """Комната со шкафом 2"""
    print(""" 
    Ты зашел в комнату, в которой 2 двери.
    Чтобы открыть дверь направо нужно отодвинуть шкаф(1). Свободный вход есть в красную(2) и черную дверь(3)""")
    choice = input("> ")
    if choice == "1":
        print("Шкаф слишком тяжелый, а ты ослаблен. Попробуй красную(2) или синюю(3) дверь.")
        choice = input("> ")
    if choice == "2":
        start_room()
    elif choice == "3":
        door_room()
    else:
        dead("Ты ходишь из стороны в сторону, и вскоре умираешь с голода.")


def door_room():
    """Комната с дверью. Тупик. Попытка подобрать ключ"""
    print("""
    Перед тобой дверь с кодовым замком из 3 цифр. Попробуешь подобрать за 5 попыток(1) или же вернешься обратно(2)?""")
    choice = input("> ")
    if choice == "1":
        for i in range(1, 6):
            key = 666
            b = input(f"Введи свой код: \n> ")
            if key == int(b):
                print("Дверь скрипнула и слегка приоткрылась. Но, к сожалению, ты не можешь туда пролезть. Придется "
                      "возвращаться обратно.")
                wardrobe_room()
            else:
                print("Код не подошел. Придеться возвращаться обратно.")
                wardrobe_room()
    elif choice == "2":
        wardrobe_room()
    else:
        dead("Ты ходишь из стороны в сторону, и вскоре умираешь с голода.")


def insect_room():
    """Комната с насекомыми"""
    print(""" 
    Ты заходишь в комнату. Она еле освещена слабым желтым светом.
    Вокруг слышно жужжание, а по полу бегают пауки. И вдруг ты понимаешь, что они уже ползают по тебе
    Ты начинаешь их смахивать и уже не понимаешь из какой двери ты вошел.
    Куда бежать: красная(1), синяя(2) или черная(3) дверь?""")
    choice = input("> ")
    if choice == "1":
        eyes_room()
    elif choice == "2":
        box_room()
    elif choice == "3":
        dog_room()
    else:
        dead("Ты ходишь из стороны в сторону, и вскоре умираешь с голода.")


def acid_room():
    """комната с кислотой"""
    print("""
    Посреди комнаты разлита какая-то бурлящая жидкость, которую вряд ли можно будет обойти.
    Вернешься обратно(1) или попробуешь перейти?(2)""")
    choice = input("> ")
    if choice == "1":
        dog_room()
    elif choice == "2":
        dead("К сожалению, кислота была слишком сильной и в итоге ты умер.")
    else:
        dead("Ты ходишь из стороны в сторону, и вскоре умираешь с голода.")


def eyes_room():
    """комната с глазами"""
    print(""" 
    Приоткрыв слегка дверь, ты видишь в темноте светящиеся глаза. Страх сковал тебя.
    Дальше идти может быть опасно. Рискнешь(1) или вернешься обратно(2)?""")
    choice = input("> ")
    if choice == "1":
        print("Что-то громко мяукнуло и исчезло. Возможно, это была кошка? В любом случае в этот раз тебе повезло."
              "Ты проходишь дальше в следующую дверь.")
        girl_room()
    elif choice == "2":
        acid_room()
    else:
        dead("Ты ходишь из стороны в сторону, и вскоре умираешь с голода.")


def girl_room():
    """комната с девочкой"""
    print(""" 
    Зайдя в комнату ты видишь маленькую девочку. На вид ей лет 5.
    Ее голова опущена и волосы скрывают ее лицо.
    Стой. В ее руках какая-то записка. Она протягивает ее тебе. 
    В голове туман и вот ты уже забыл откуда пришел.
    Возьмешь записку(1) или пройдешь дальше? Ты видишь 3 двери: синяя(2), желтая(3), красная(4)""")
    choice = input("> ")
    if choice == "3":
        end_room()
    elif choice == "2":
        eyes_room()
    elif choice == "4":
        box_room()
    elif choice == "1":
        dead("Ты взял записку в руки и девочка внезапно подняла голову. Ты ужаснулся. На окровавленном лице полностью "
             "отсутствовали глаза. Неожиданно свет погас. Тебя убили.")
    else:
        dead("Ты ходишь из стороны в сторону, и вскоре умираешь с голода.")


def box_room():
    """комната с ящиком"""
    print(""" 
    Посреди комнаты стоит большой деревянный ящик. Внутри явно что-то или кто-то есть.
    Он закрыт железными цепями, но замок на нем приоткрыт и его можно легко снять.
    Откроешь ящик(1), или откроешь красную(2) или черную(3) дверь?""")
    choice = input("> ")
    if choice == "2":
        girl_room()
    elif choice == "3":
        acid_room()
    elif choice == "1":
        dead("Ты открыл ящик. Внутри оказалась какая-то субстанция черного цвета. Ты потерял сознание и в итоге умер.")
    else:
        dead("Ты ходишь из стороны в сторону, и вскоре умираешь с голода.")


def end_room():
    """Последняя комната"""
    print(""" 
    Ты успешно дошел до выхода! Поздравляю!
    """)
    exit(0)


print("Поиграем?"
      "Для выбора действия в скобочках указаны цифры - вводи их без скобок или дополнительных символов."
      "Поехали!")
start()
