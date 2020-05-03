## a dizisinin içinde tekler başa çiftler sona ##

a = [0,1,2,3,4,5,6,7,8,9]
kosul = len(a)
k = 0 
##l = 1
temp = 0
print(a)
for i in range(kosul):
    if a[i]%2 ==1:
        temp = a[i]
        a[i] = a[k]
        a[k] = temp
        k+=1
    

        

print(a)
