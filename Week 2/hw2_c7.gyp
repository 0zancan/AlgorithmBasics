sayiAdedi = int (input("Kaç sayı girmek isterisniz: "))
ortanca = 0

for i in range(sayiAdedi):
    sayi = int (input("Sayi giriniz: "))
    if buyuk < sayi:
        buyuk = sayi
        

print("Ortanca sayı = {}".format(ortanca))