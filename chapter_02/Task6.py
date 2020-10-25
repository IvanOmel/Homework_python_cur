disguise_purchases = round(float(input("ввести величину покупки: ")), 2)

federal_tax = disguise_purchases * 0.05
print("федеральный налог с продаж: ", round(federal_tax, 2))

regional_tax = disguise_purchases * 0.025
print("региональный налог с продаж: ", round(regional_tax, 2))

general_sales_tax = regional_tax + federal_tax
print("общий налог с продаж: ", round(general_sales_tax, 2))

total_sale_amount = disguise_purchases + general_sales_tax
print("Итоговуя суммаж: ", round(total_sale_amount, 2))
