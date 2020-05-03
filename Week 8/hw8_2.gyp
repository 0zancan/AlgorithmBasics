# Klavyeden girilen sayıdan dizide kaç tane olduğunu 
# ekrana yazdıran program

a = [5,5,3,7,8,5,7,7,7,3,8,9,8,9,8,8,15,5,8,4]
n = len(a)
sayac = 0
girdi = int(input("Bir sayı giriniz: "))

for i in range(n):
    if girdi == int(a[i]):
        sayac += 1

print("Girdiğiniz {} sayısı, dizide {} adet bulunmaktadır."
.format(girdi,sayac))
