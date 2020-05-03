


# a ve b dizilerinin birleşimlerini c dizinsinde
# sıralı yazan program!

a = [-1, 4, 6, 7, 12, 15, 16, 26, 27, 34]
b = [3, 5, 9, 20, 23, 30, 37, 39, 41, 45]
n = len(a) #10
c = 20*[None]
r = len(c)
k=0
for i in range(r):
    if i < n:
        c[i] = a[i]
    else:
        c[i] = b[k]
        k += 1
print(c)
temp = 0
for i in range(r):              
    for j in range(i,r):        
        if c[i] > c[j]:           
            temp = c[j]
            c[j] = c[i]
            c[i] = temp

print(c)

