# 10 elemanlı bir dizi 11. elemanı kullanıcı girsin
# Dizi büyükten küçüğe sıralı
# 11. elemanı sıraya göre uygun bir yere yerleştir.

a = [45,40,35,30,25,20,15,10,5,4,None]
# [45 40 35 30 25 20 15 10 5 1]
n = len(a)
temp = 0

number = int(input("Write a number: "))

for i in range(n-2):
    if int(a[i]) > number >= int(a[i+1]):
        for j in range((n-1),(i+1),-1): 
            # i+1 e number i yazmalıyım!
            a[j] = a[j-1]
        a[i+1] = number 
    elif number < a[n-2]: # küçükse en sona yazdır!
        a[n-1] = number
    elif number > a[0]: # büyükse bi yana kaydır en başa koy
        for j in range(n-1,0,-1):
            a[j] = a[j-1]
        a[0] = number
print(a)