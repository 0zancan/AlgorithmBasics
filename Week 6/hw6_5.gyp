# 11-> Klavyeden girilen n'ye göre 
# örnekteki gibi desen yazdırma 
# Örnek: n=5 
# Çıktı:
"""
* * * * *
* * * *
* * *
* * 
*

"""
n = input("n: ")
n = int(n)
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()

n = input("n: ")
n = int(n)
for i in range():
        print("*",end="")
    for j in range(i):
    print()