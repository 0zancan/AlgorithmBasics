# a dizisindeki tek sayıları b dizisinin başına,
# çift sayıları b dizisinin sonuna yerleştiren program
# (sıra önemli değil)

a = [4,8,3,1,18,9,21,20,5,17,78]
b = 11*[None]
n = (len(a))
tek = 0
cift = n-1

for i in range(n):
    if a[i]%2 != 0: #tek
        b[tek]= a[i]
        tek+=1
    else: #çift
        b[cift] = a[i] 
        cift-=1  

print(b)