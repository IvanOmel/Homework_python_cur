
cost = round(float(input("ввести стоимость еды: ")), 2)

tip = cost * 0.18
print("размер 18-процентных чаевых: ", round(tip, 2))

tax = cost * 0.07
print("7-процентного налога с продаж: ", round(tax, 2))

total_amount = tip + tax + cost
print("Итоговуя сумма: ", round(total_amount, 2))