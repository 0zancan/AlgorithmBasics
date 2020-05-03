# Dizinin elemanlarını küçükten büyüğe sıralama

a = [1,8,4,3,18,9,21,20,5,17,78]
n = (len(a))
temp = 0
for i in range(n):              
    for j in range(i,n):        
        if a[i]>a[j]:           
            temp = a[j]
            a[j]=a[i]
            a[i] = temp

print(a)