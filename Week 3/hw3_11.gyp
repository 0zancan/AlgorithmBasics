# Klavyeden a ve b giriliyor.
# a ile b arasındaki 5'in katlarını ekrana yazdıran program
# a ve b dahil değil

a = int (input("a sayisini giriniz: "))
b = int (input("b sayısını giriniz: "))

for a in range(a,b):
    if a%5 == 0:
        print(a)

