# Dizinin toplamını ve ortalamasını ekrana yazdıran program

a = [4,8,3,1,18,9,21,20,5,17]
n = len(a)
toplam = 0
for i in range(n):
    toplam += int(a[i])
    ortalama = toplam/n

print("Toplam: {}\nOrtalama: {}".format(toplam,ortalama))