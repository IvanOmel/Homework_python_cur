
mass = float(input("Input mass: "))

weight = mass * 9.8

if(weight >= 500):
    print("weight: ", round(weight, 2), "H")
    print("body is too heavy")
elif(weight <= 100):
    print("weight: ", round(weight, 2), "H")
    print("body is too light")
else:
    print("weight: ", round(weight, 2), "H")
    print("body is ok")