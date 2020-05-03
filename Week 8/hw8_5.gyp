# a ve b dizilerinin birleşimlerini yaz!

a = [4,8,3,1,18,9,21,20,5,17]
b = [8,13,6,12,4,5,19,1,14,25,11]

n = len(a)
p = len(b)
for i in range(n):
    print(a[i], end=" ")

for i in range(n):
    flag = 0
    for j in range(p): # tekrar ediyo mu
        if b[i] == a[j]: ###
            flag = 1
    if flag == 0:
        print(b[i], end =" ")