shares = 2000
paid = 40.0
broker_commission = 0.03
sold = 42.75
print("Вывод даных:")
sum_paid = round(shares * paid, 2)
print("сумму денег, уплаченную за акции: ", sum_paid)
paid_broker_commission = round(sum_paid * broker_commission)
print("сумму комиссии, уплаченную брокеру при покупке акций: ", paid_broker_commission)
sum_sold = round(shares * sold, 2)
print("сумму, за которую продал акции: ", sum_sold)
sold_broker_commission = round(sum_sold * broker_commission, 2)
print("сумму комиссии, уплаченную брокеру при продаже акций: ", sold_broker_commission)

fin = (sum_sold - sum_paid) - (paid_broker_commission + sold_broker_commission)

if (fin > 0):
    profit = fin
    print("получил прибыль:", round(profit))
else:
    damages = fin
    print("понес убытки: ", round(damages))
