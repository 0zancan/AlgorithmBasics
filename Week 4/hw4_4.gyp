# Dizinin son n adet elemanını baştan sona 
# doğru yazdıran program

a = [4,8,3,1,18,9,21,20,5,17]
uzunluk = len(a)
n = int(input("Kaç eleman görmek istiyorsun: "))


for i in range(uzunluk):
    if uzunluk-n <= i:
        print(a[i])