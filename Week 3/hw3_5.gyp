# Klavyeden girilen 5 sayıyı toplayan prgoram

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