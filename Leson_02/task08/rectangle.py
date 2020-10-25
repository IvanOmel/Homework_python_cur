def rectangle():
    h = round(float(input("Input height: ")))
    w = round(float(input("Input width: ")))

    print("*" * w)

    for i in range(0, h - 2):
        print("*" + (" " * (w - 2)) + "*")

    print("*" * w)

rectangle()