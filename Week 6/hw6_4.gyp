# 10 -> klavyeden girilen n'ye göre belirtilen deseni
# ekrana yazdıran program
# Desen: *
# Örnek: Sayı: 3
# Çıktı:   
"""
            *

            *
            *

            *
            *
            *

"""


n = input("n: ")
n = int(n)
for i in range(n):
    for j in range(i+1):
        print("*")
    print()

