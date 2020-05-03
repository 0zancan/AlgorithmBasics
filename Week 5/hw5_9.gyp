# Dizinin en küçük elemanını dizinin 
# ilk elemanıyla yer
# değiştiren program

a = [4,8,3,1,18,9,21,20,5,17,78]
n = (len(a))
kucuk = a[0]
indis = 0
temp = 0
for i in range(1,n):      
    if kucuk > a[i]:
        kucuk = a[i]
        indis = i

a[indis] = a[0]
a[0] = kucuk

#temp gereksiz!

print(a)     
print("Dizideki en küçük sayı: ",kucuk)
print("Dizideki en büyük sayının indisi: ",indis)
