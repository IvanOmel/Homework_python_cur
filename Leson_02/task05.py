n = round(float(input("Input N: ")))

n_f = 1

for i in range(1, n + 1):
     n_f *= i

print("n!: ", n_f)

n_f_min_1 = 1

for j in range(1, n):
     n_f_min_1 *= j

print("(n-1)!: ", n_f_min_1)

fin = n_f * (n_f - (n * n_f_min_1))

print("n!( n! - n * (n - 1)!) = ", fin)