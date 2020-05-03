# n klavyeden girilen pozitif bir sayıdır.
# 1'den n'ye kadar olan sayıların toplamını ekrana yazdıran program

n = int (input("Pozitif bir tam sayı giriniz: "))
toplam = 0

for i in range(n):
    toplam +=i
print(toplam)
    

