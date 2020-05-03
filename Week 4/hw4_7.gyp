# Dizinin elemanlarını bir öne kaydıran ve dizinin ilk
# elemanını sona atayan program
"""
#v1
a = [4,8,3,1,18,9,21,20,5,17]
n = len(a)

a.append(a[0])

for i in range(n):
    a[i]=a[i+1]
a.remove(a[n])
print(a)
"""

"""
#v2
a = [4,8,3,1,18,9,21,20,5,17]
a.append(a[0])
a.remove(a[0])
print(a)
"""

#v3
a = [4,8,3,1,18,9,21,20,5,17]
n = len(a)-1
temp = a[0]
for i in range(n):
    a[i]=a[i+1]
a[n] = temp
print(a)