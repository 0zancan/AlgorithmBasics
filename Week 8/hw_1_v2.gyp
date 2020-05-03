# 10 elemanlı bir dizi 11. elemanı kullanıcı girsin
# Dizi büyükten küçüğe sıralı
# 11. elemanı sıraya göre uygun bir yere yerleştir.

a = [45,40,35,30,25,20,15,10,5,4,0]
n = len(a)
min = a[n-2]

number = int(input("Write a number: "))

for i in range(n-2,-1,-1):
    if number <= min:
        a[n-1] = number
    elif number > a[i]:
        a[i+1] = a[i]
        a[i] = number 

print(a)