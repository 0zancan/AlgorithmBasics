# Klavyeden girilen sayıdan küçük ve tek olan 
# elemanları ekrana yazdıran program

"""
toplam = 0
#i = True
while True:
    sayi = input("Bir sayı girebilir veya toplamı görmek için 'q' ya basabilirsiniz: ")
    if sayi != "q":
        toplam += int(sayi)
    else:
        print("Girilen sayının toplamı = ", toplam)
        # i=False
        break
"""

a = [4,8,3,1,18,9,21,20,5,17]
sayi = int(input("Bir sayı giriniz: "))
n = len(a)
toplam = 0
for i in range(n):
    if a[i] < sayi and a[i]%2 != 0:
        print(a[i])
