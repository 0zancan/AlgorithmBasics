# 9-> 1. elemanını 1, 2. elemanını 2
# 3. elemanını 3... defa yazdıran program 

a = [4,8,3,1,18,9,21,20,5,17,78]
n = (len(a))
for i in range(n):
   # m = i+1
    for j in range((i+1)):
        print(a[i])