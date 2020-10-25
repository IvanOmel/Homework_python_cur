def rhombus():
    size = round(float(input("Input size: ")))

    j = 1

    for i in range(0, size):
        print((" " * (size - i)) + ("*" * j))
        j += 2

    a = 0

    for k in range(0, size + 1):
        print((" " * a) + ("*" * (size - k)) + ("*" * (size - (k - 1))))
        a += 1


rhombus()
