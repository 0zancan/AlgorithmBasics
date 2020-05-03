# Klavyeden bir sayıyı basamaklarına ayıran program "7235"

sayi = input("Bir sayi giriniz: ")
n = len(sayi)-1
k=1
for i in range(n,-1,-1):  
    print("{}'ler basamağı {}".format(k,sayi[i]))
    k=k*10

