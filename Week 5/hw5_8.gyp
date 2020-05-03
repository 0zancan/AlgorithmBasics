# Dizinin en büyük elemanını ve indis numarasını yazdıran program

a = [4,8,3,1,18,9,21,1502,20,5,17,78]
n = (len(a))
buyuk = 0
indis = 0
for i in range(n):      
    if buyuk < a[i]:
        buyuk = a[i]
        indis = i
print("Dizideki en büyük sayı: ",buyuk)
print("Dizideki en büyük sayının indisi: ",indis)
