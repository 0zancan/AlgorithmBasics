# Klavyeden sürekli sayı giriliyor
# 1,2,3 girildiğinde programdan çıkılıyor
# Sayıların sırası ve
# ardışıklığı önemli değil

bir=False
iki=False
uc=False
kosul = bir+iki+uc
while kosul < 3:
    sayi = int(input("Sayi giriniz: "))
    if sayi == 1:
        bir = True
    elif sayi == 2:
        iki = True
    elif sayi == 3:
        uc = True
    kosul = bir+iki+uc