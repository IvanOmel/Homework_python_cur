print("Start")
print("*" * 100)

products = [0] * 5
for i in range(0, 5):
    print("Товар №", i + 1)
    products[i] = round(float(input("Введите цену товара: ")), 2)

print("Стоимость приобретаемых товаров: ", round(sum(products), 2))
print("Налог с продаж составляет 7%")

tax = 0.07
sales_tax_amount = sum(products) * tax
print("Сумма налога с продаж: ", round(sales_tax_amount, 2))

total_amount = sales_tax_amount + sum(products)
print("Итоговуя сумма: ", round(total_amount, 2))

print("*" * 100)
print("End")
