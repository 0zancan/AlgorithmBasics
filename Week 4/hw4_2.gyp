# Klavyeden girilen sayıdan küçük, tek ve çift
# dizi elemanlarının toplamını ve adetlerini ekrana
# ayrı ayrı yazdıran program
# 23/04/2020

a = [4,8,3,1,18,9,21,20,5,17]
sayi = int(input("Bir sayı giriniz: "))
n = len(a)
tekToplam = 0
tekAdet = 0
ciftAdet = 0
ciftToplam = 0
for i in range(n):
    if a[i] < sayi and a[i]%2 != 0: # küçük, tek
        tekToplam += a[i]
        tekAdet += 1
    elif a[i] < sayi and a[i]%2 == 0: # küçük, çift
        ciftToplam += a[i]
        ciftAdet += 1

print("Küçük ve Tek Sayıların Toplamı: ",tekToplam)
print("Toplam tek sayı adedi: ", tekAdet)
print("Küçük ve Çift Sayıların Toplamı: ",ciftToplam)
print("Toplam çift sayı adedi: ", ciftAdet)