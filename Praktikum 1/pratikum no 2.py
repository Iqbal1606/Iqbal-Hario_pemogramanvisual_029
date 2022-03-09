# Nama  : Iqbal Hario syahputra
# NIM   : 20051397029
# Kelas : D4 Manajemen Informatika 2020A

print("-" * 80)
a = 1
while a <= 10:
    n = 1
    while n <= 10:
        print("| %4d |" % (a*n), end="")
        n = n + 1
    print(""),
    a = a + 1
print("-" * 80)
