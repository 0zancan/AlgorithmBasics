# Klavyeden s ve n giriliyor.
# Dizinin s nolu elemanından başlayarak n adet
# elemanı kendi içinde tersine çeviren program

a = [4,8,3,1,18,9,21,20,5,17,78]
n = (len(a))

ozan = int(input("ozan: ")) # indis olarak aldım
ahmet = int(input("ahmet: "))

for i in range(ozan,ahmet):      
    if ozan<=i<ahmet+ozan:
        temp = a[i]         # temp = 4 , 8 
        a[i] = a[n-1-i]     # a[0,1] = a[9,8] = 5
        a[n-1-i] = temp     # a[9,8] = 8
print(a)