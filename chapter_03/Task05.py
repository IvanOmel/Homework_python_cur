amount1 = float(input("Введите  значение amount1: "))
amount2 = float(input("Введите  значение amount2: "))


if (amount1 > 10):
    if (amount2 < 100):
        array = [amount1, amount2]
        print("большее значение из двух переменных: ", max(array))
    else:
        print("amount2 > 100")
else:
    print("amount1 < 10")

