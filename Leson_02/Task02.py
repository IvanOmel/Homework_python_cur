k = round(float(input("Input K: ")))

while True:
    n = round(float(input("Input N: ")))
    if n > 0:
        i = 0
        while i < n:
            print(i, ":", k)
            i += 1
        break

    else:
        print("Error Try again")