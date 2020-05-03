# a ve b nin kesişimlerini yazdıran program

a = [4,8,3,1,18,9,21,20,5,17,25]
b = [8,13,6,12,4,5,19,1,14,25]

k = len(a)
l = len(b)

for i in range(k):
    for j in range(l):
        if a[i] == b[j]:
            print(a[i])

