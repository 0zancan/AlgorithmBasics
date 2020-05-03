# 8-> dizinin her elemanını kendisi kadar yazdıran program

a = [4,8,3,1,18,9,21,20,5,17,78]
n = (len(a))
for i in range(n): # tüm elemanları gez
    for j in range(a[i]): # elemanın kendisine kadar git
        print(a[i])       # elemanı yazdır 
