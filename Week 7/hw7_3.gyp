# Klavyeden sürekli sayı giriliyor.
# Arka arkaya 1 2 3 girildiğinde programdan çıkılıyor

sayi = 100*[None]
i=0
flag = 1
while flag:
    sayi[i] = input("Sayi giriniz: ")
    if sayi[i]=="3" and sayi[i-1]=="2" and sayi[i-2]=="1" : 
        flag = 0
    i+=1