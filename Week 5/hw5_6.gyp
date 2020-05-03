# a dizisinin içinde tekler başa çiftler sona 

a = [4,8,3,1,18,9,21,20,5,17,78]
#a = [0,1,2,3]
n = (len(a))
tek = 0
cift = n-1
temp = 0
print(a)
while cift!=tek:
    if a[tek]%2 != 0: #tek
        tek+=1
    else:
        temp = a[cift]
        a[cift] = a[tek] 
        a[tek] = temp
        cift-=1  
print(a)

## 

a = [4,8,3,1,18,9,21,20,5,17,78]
kosul = len(a)
k = 0 
temp = 0
print(a)
for i in range(kosul):
    if a[i]%2 == 1:
        temp = a[i]
        a[i] = a[k]
        a[k] = temp
        k+=1
print(a)