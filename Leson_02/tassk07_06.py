x = round(float(input("Input x: ")))
n = round(float(input("Input N: ")))

i = 0
p = 1

while i < n:
    p *= x
    i += 1

print("x^N = ", p)