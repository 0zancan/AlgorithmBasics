# a'yı kendi içerisinde tersine çeviren program

a = [4,8,3,1,18,9,21,20,5,17,78]
n = (len(a))
m = int(n/2)
for i in range(m):      # i = 0 , 1
    temp = a[i]         # temp = 4 , 8 
    a[i] = a[n-1-i]     # a[0,1] = a[9,8] = 5
    a[n-1-i] = temp     # a[9,8] = 8
                        # [*17* 8 3 1 18 9 21 20 5 *4*]
print(a)                
