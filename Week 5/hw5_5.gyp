# Son n elemanı sondan başa yazdıran program

a = [4,8,3,1,18,9,21,20,5,17]
son = len(a)-1
n = int(input("Kaç eleman görmek istiyorsun: "))

for son in range(son,n-1,-1):
    print(a[son])