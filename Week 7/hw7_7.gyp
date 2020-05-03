# Klavyeden sürekli sayı giriliyor. 
# Sayılar toplanıyor, toplam 1000'i geçinc
# son toplam ekrana yazdırılıyor, 
# program sonlanıyor

toplam = 0
flag = 1

while flag:
  toplam += int(input("Sayi giriniz: "))
  if toplam >= 1000:
    flag = 0

print("Toplam: ",toplam)