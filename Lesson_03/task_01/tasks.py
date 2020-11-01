def first():
    array = []

    i = 0

    while 10 > len(array):
        if i % 2 != 0:
            array.append(i)

        i += 1

    print(array)


def second():
    array_pos = []
    array_neg = []
    for i in range(10):
        print("Input number", i + 1, ": ", end="")
        quest = round(float(input()))

        if i % 2 != 0:
            array_neg.append(quest)
        else:
            array_pos.append(quest)
    print("четные: ", array_pos)
    print("нечетные: ", array_neg)


def three():
    array_pos = []
    array_neg = []
    for i in range(10):
        print("Input number", i + 1, ": ", end="")
        quest = round(float(input()))

        if i % 2 != 0:
            array_neg.append(quest)
        else:
            array_pos.append(quest)
    print("четные: ", len(array_pos))
    print("нечетные: ", len(array_neg))


def four():
    array_pos = []
    array_neg = []
    for i in range(10):
        print("Input number", i + 1, ": ", end="")
        quest = round(float(input()))

        if i % 2 != 0:
            array_neg.append(quest)
        else:
            array_pos.append(quest)
    print("четные сумма елементов: ", sum(array_pos))
    print("нечетные сумма елементов: ", sum(array_neg))

    print("четные среднее арифметическое: ", (sum(array_pos) / len(array_pos)))
    print("нечетные среднее арифметическое: ", (sum(array_neg) / len(array_neg)))


def five():
    array_pos = []
    array_neg = []
    for i in range(10):
        print("Input number", i + 1, ": ", end="")
        quest = round(float(input()))

        if i % 2 != 0:
            array_neg.append(quest)
        else:
            array_pos.append(quest)

    print("четные: ", array_neg)
    print("нечетные: ", array_pos)

    for j in range(len(array_neg)):
        if j % 2 != 0:
            array_pos[j - 1] = array_neg[j]

    print("New array: ", array_pos)


def six():
    n = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    min_n = min(n)

    if n.count(min_n) != 1:
        print("Index of min element in array N: ", n.index(min_n))
    else:
        print("Min of array N: ", min_n)


def seven():

    array = [4, -5, 0, 6, 8]

    print("Old array: ", array)

    max_e = max(array)

    i_max = array.index(max_e)

    min_e = min(array)

    i_min = array.index(min_e)

    array[i_max] = min_e
    array[i_min] = max_e

    print("New array: ", array)