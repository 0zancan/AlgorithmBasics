# Dizide en çok tekrarlanan sayısı ve adedini bulan program
# Dizi sayıları sıralı

a = [1,1,1,1,1, 1,1,3, 5, 5, 8, 9, 17, 17,17,17,17 ,20, 24,24,24,24,24,24,24]
n = len(a)-1

temp = 1
sum = 0 # tekrar sayısı
repNumber = 0 # hangi eleman

for i in range(n):
    if a[i] == a[i+1]:
        temp += 1
    else:
        temp = 1
    if temp >= sum:
        sum = temp
        repNumber = a[i]

print("Dizide en çok tekrarlanan sayı: {},\nTekrarlanma sayısı: {}"
      .format(repNumber, sum))
