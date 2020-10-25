print("Рецепт-калькулятор:")

number = int(input("сколько булочек хочеш приготовить: "))
recept_number = number / 48

sugar = recept_number * 1.5
oil = recept_number
flour = recept_number * 2.75

print("Рецепт булочек предусматривает ингредиенты: ")
print(round(sugar, 2), " стакана сахара;")
print(round(oil, 2), " стакан масла; ")
print(round(flour, 2), " стакана муки.")
print("С таким количеством ингредиентов этот рецепт позволяет приготовить ", number, "булочек.")