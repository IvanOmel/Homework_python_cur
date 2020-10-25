score = int(input("Введіть оцінку в 5-бальній системі: "))
А_score = 5
В_score = 4
С_score = 3
D_score = 2
if score >= А_score:
    print('Ваш уровень - А.')
else:
    if score >= В_score:
        print('Ваш уровень - В. ')
    else:
        if score >= С_score:
            print('Ваш уровень - С. ')
        else:
            if score >= D_score:
                print('Baш уровень - D.')
            else:
                print('Ваш уровень - F. ')
