# Dizide en çok tekrarlanan sayısı ve adedini bulan program
# Dizi sayıları sıralı +

a = [1, 1, 1, 3, 5, 5, 8, 9, 17, 17, 17, 17, 20, 24, 24]
n = len(a)
b = 2*n*[1]
k = 0
sum = 1

for i in range(n):
    for j in range(i, n):
        if a[i] == a[j]:
            sum += 1
    b[k] = a[i]
    b[k+1] = sum
    k += 2
    sum = 1
print(b) 


max = b[1]
for i in range(3, n, 2):
    if b[i] > max:
        max = b[i]

print("Dizi en çok tekrarlanan sayı: {},\nTekrarlanma sayısı: {}"
      .format(b[i-1], max))
