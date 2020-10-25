def calculate_income(rate, money, month):
    if money <= 0:
        return 0

    for i in range(1, month + 1):
        money = round(money + money * rate / 100 / 12, 2)
    return money


def grn_to_dol(money):
    dol = money / 28.30
    return round(dol, 2)



