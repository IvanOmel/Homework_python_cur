def equilateral_triangle():
    size = round(float(input("Input size: ")))
    j = 1

    for i in range(0, size):
        print((" " * (size - i)) + ("*" * j))
        j += 2


equilateral_triangle()