NumberQuarter = input('\nВведите четверть плоскости от 1 до 4: ')
while(True):
    if(NumberQuarter == '1'):
        print(f'\nДиапозон возможных коордтнат в {NumberQuarter} четверти от (0,0) до (+∞,+∞)\n')
        break
    elif(NumberQuarter == '2'):
        print(f'\nДиапозон возможных коордтнат в {NumberQuarter} четверти от (0,0) до (-∞,+∞)\n')
        break
    elif(NumberQuarter == '3'):
        print(f'\nДиапозон возможных коордтнат в {NumberQuarter} четверти от (0,0) до (-∞,-∞)\n')
        break
    elif(NumberQuarter == '4'):
        print(f'\nДиапозон возможных коордтнат в {NumberQuarter} четверти от (0,0) до (+∞,-∞)\n')
        break
    else:
        NumberQuarter = input("\n==>>Вы ввели неверные данные!!!<<==\nВведите четверть плоскости повторно от 1 до 4: ")