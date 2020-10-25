n = round(float(input("Input N: ")))

n_f = 1
i = 1

while i < n + 1:
     n_f *= i
     i += 1

n_f_min_1 = 1
i = 1

while i < n:
     n_f_min_1 *= i
     i += 1

fin = n_f * (n_f - (n * n_f_min_1))

print(fin)