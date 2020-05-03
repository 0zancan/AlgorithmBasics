# Dizide en çok tekrarlanan sayısı ve adedini bulan program
# Dizi sayıları sıralı

a = [1, 1, 1,1,1,1,1,1, 3, 5, 5, 8, 9, 17, 17, 17, 17, 20, 24]
n = len(a)

temp = 1
sum = 0
repNumber = 0

for i in range(n):
    for j in range(i+1, n):
        if a[i] == a[j]:
            temp += 1
    if temp > sum:
        sum = temp
        repNumber = a[i]
    temp = 1

print("Dizi en çok tekrarlanan sayı: {},\nTekrarlanma sayısı: {}"
      .format(repNumber, sum))
