

array = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

while (True):

    number = int(input("Input number: "))

    if (1 <= number and number <= 10):
        print("Rome numbers: ", array[number - 1])
        break
    else:
        print("Error. Try again.")
