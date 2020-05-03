# 15 elemanlı küçükten büyüğe sıralanmış diziyi
# her sayıdan 1 tane kalacak şekilde düzenleyen
# bu sayıları dizinin başında biriktiren ve geri
# kalan sayıları sıfırlayan program.

a = [1,1,1,3,5,5,8,9,17,17,17,24,24,24,24]
n = len(a)
temp = 0
size = 0

#--  tekrar edenleri sıfırlama
for i in range(n-1):
    for j in range(i+1,n):
         print(a[i])
         if a[i] == a[j]: 
             a[j]=0
print(a)
## -------------------------------------


# # --- dizideki 0 ların sayısını bulma
for i in range(n):
    if a[i] == 0:
        size += 1
print(size)
## -------------------------------------

# diziyi küçükten büyüğe sıralama 
for i in range(n):              
    for j in range(i,n):        
        if a[i]>a[j]:           
            temp = a[j]
            a[j]=a[i]
            a[i] = temp
print(a)
## -------------------------------------


# dizideki sıfırları en sona atma
for i in range(size+1):
    a[i] = a[size]
    a[size] = 0
    size += 1 
print(a)
## -------------------------------------
