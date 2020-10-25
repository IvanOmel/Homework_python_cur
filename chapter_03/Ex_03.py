age = float(input("Input your age: "))

if(age <= 1):
    print("младенец")
elif(1 < age and age < 13):
    print("ребенок")
elif(13 <= age and age < 20):
    print("подросток")
else:
    print("взрослый")

