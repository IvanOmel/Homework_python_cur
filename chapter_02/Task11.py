print("List: ")
boys = int(input("number of boys: "))
girls = int(input("number of girls: "))

pupils = boys + girls

boys_per = round((boys / pupils), 2) * 100
girls_per = round((girls / pupils), 2) * 100

print("Pupils: ", pupils)
print("boys: ", boys_per, "%")
print("girls: ", girls_per, "%")