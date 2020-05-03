# 7-> dizinin her elemanını 5 defa yazdıran program

a = [4,8,3,1,18,9,21,20,5,17]
n = len(a)
b = n*[None]

for i in range(n):          # i = 0
    b[i] = a[n-1-i]         # b[0] = a[10-1-0] = 17
print(b)