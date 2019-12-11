# Оператор continue начинает следующий проход цикла, минуя оставшееся тело цикла (for или while)
for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')
