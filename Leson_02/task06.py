x = round(float(input("Input x: ")))
n = round(float(input("Input N: ")))

p = 1

for i in range(0, n):
    p *= x

print("x^N = ",p)