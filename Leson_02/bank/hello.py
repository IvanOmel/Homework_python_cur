#! Программа Банковский счет
from bank import account

rate = int(input("Введите процентную ставку: "))
money = int(input("Введите сумму, грн: "))
money_grn = money
period = int(input("Введите период ведения счета в месяцах: "))

result = account.calculate_income(rate, money, period)
print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n","Период: ", period, "\n", "Сумма на счете в конце периода: ", result)

print("Сумма: ", money_grn)

print("Сумма в доларах: ", account.grn_to_dol(money_grn))
