# a dizisinin en büyük elemanını 
# bulan program

a = [4,8,3,1,18,9,21,20,5,17,78]
n = (len(a))
buyuk = a[0] 
for i in range(n):      
    if buyuk < a[i]:
        buyuk = a[i]
print("Dizideki en büyük sayı: ",buyuk)
