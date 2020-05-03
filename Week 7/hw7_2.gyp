# Klavyeden girilen bir sayının tersinden
# yeni bir sayı elde eden program
"""
sayi = input("Bir sayi giriniz: ")
n = len(sayi)-1
k=1
for i in range(n,-1,-1):  
    print(sayi[i],end="")
    print()
"""
### 

sayi = input("Bir sayi giriniz: ")
n = len(sayi)-1
k= 0
yeniSayi = (n+1)*[None] 
for i in range(n,-1,-1):  
    yeniSayi[k]=sayi[i]
    k+=1

print()
