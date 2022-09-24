number = int(input("Введите выходной день недели от 1 до 7: "))
weekday = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресение']
while(True):
    if(number > 0 and number < 8):
        if(number == 6 or number == 7):
            print(f'Да, это выходной день, {weekday[number - 1]}')
        else:
            print(f'Нет, это будний день, {weekday[number - 1]}')
        break
    else:
        number = int(input("==>>Вы ввели неверные данные!!!<<==\nВведите день недели повторно от 1 до 7: "))
