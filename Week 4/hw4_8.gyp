# Klavyeden girilen sayıdan küçük dizi elemanlarını
# ekrana yazdıran program

a = [4,8,3,1,18,9,21,20,5,17]
sayi = int(input("Bir sayı giriniz: "))
n = len(a)
toplam = 0
for i in range(n):
    if a[i] < sayi:
        print(a[i])
