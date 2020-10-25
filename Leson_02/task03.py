while True:

    a = round(float(input("Input a: ")))
    b = round(float(input("Input b: ")))

    if a < b:
        for i in range(a, b + 1):
            print(i)
        count = range(a, b + 1)
        print("N = ", len(count))
        break
    else:
        print("a > b : Error try again")