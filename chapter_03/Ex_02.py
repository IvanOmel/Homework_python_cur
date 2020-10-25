# Площади прямоугольников

length_first = float(input("Input length first: "))
width_first = float(input("Input width first: "))

area_first = length_first * width_first

length_second = float(input("Input length second: "))
width_second = float(input("Input width second: "))

area_second = length_second * width_second

if(area_first > area_second):
    print("area first > area second")
    print("area first = ", area_first)
elif(area_first < area_second):
    print("area first < area second")
    print("area second = ", area_second)
else:
    print("area first == area second")
    print("area first = ", area_first)
    print("area second = ", area_second)
