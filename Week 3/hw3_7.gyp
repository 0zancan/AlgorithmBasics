# a[] = {4,8,3,1,18,9,21,20,5,17};
# Dizinin elemanlarının toplamını ekrana yazdıran program. 

a = [4,8,3,1,18,9,21,20,5,17]
n = len(a)
toplam = 0
for i in range(n):
    toplam += a[i]

print("Dizinin toplamı = ", toplam)