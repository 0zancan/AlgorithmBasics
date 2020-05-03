sayiAdedi = int (input("Kaç sayı girmek isterisniz: "))
buyuk = 0

for i in range(sayiAdedi):
    sayi = int (input("Sayi giriniz: "))
    if buyuk < sayi:
        buyuk = sayi

print("En büyük sayı = {}".format(buyuk))


""" v1
sayiAdedi = int (input("Kaç sayı girmek isterisniz: "))
buyuk = 0
sayilar = []

for i in range(sayiAdedi):
    sayi = int (input("Sayi giriniz: "))
    sayilar.append(sayi)
    if buyuk < sayilar[i]:
        buyuk = int(sayilar[i])

print("En büyük sayı = {}".format(buyuk))
"""