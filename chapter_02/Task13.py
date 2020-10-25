print("ввести: ")

ridge_length = float(input("длину гряды в метрах: "))
volume_space_occupied_end_support = float(input("объем пространства, занимаемого концевой опорой в метрах: "))
amount_space_between_vines = float(input("объем пространства между виноградными лозами в метрах: "))

r = ridge_length
e = volume_space_occupied_end_support
s = amount_space_between_vines

number_of_vines = (r - (2 * e)) / s

print("количество виноградных лоз, которые поместятся на гряде: ", round(number_of_vines, 2))
