# Klavyeden girilen sayıdan dizide olup olmadığını
# söyleyen program

a = [5,5,3,7,8,5,7,7,7,3,8,9,8,9,8,8,15,5,8,4]
n = len(a)
flag = 0
girdi = int(input("Bir sayı giriniz: "))

for i in range(n):
    if girdi == int(a[i]):
        flag = 1

if flag == 1:  
    print("Girdiğiniz {} sayısı, dizide bulunmaktadır.".format(girdi))
else:
    print("Girdiğiniz {} sayısı, dizide bulunMAMAKtadır.".format(girdi))