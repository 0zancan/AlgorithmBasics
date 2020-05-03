# Dizinin ilk n elemanını dizinin sonuna atayan ve baştaki
# elemanları sıfırlayan program

a = [4,8,3,1,18,9,21,20,5,17]
uzunluk = len(a)
n = int(input("n sayısı: "))

for i in range(uzunluk-n):
    if i<n:
        a[uzunluk-n+i] = a[i]
        a[i]=0
    else:
        a[i] = 0

for i in range(uzunluk):
    print(a[i])
