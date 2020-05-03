# n klavyeden girilen 1 ile 10 arasında bir sayıdır,
# Dizinin ilk n adet elemanını ekrana yazdıran program

a = [4,8,3,1,18,9,21,20,5,17]
n = int(input("Kaç eleman görmek istiyorsun: "))

for i in range(n):
    print("Dizinin {}. adet elemanı: {}".format(i+1,a[i]))