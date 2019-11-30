
with open('test.txt', 'wt', encoding='UTF-8') as InFile:
    num = int(input("Введите число: "))
    line = str('1 / ' + str(num) + ' = ' + str(1 / num))
    print(line)
    InFile.write(line)
