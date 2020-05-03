# Dizideki tek sayıları ve tek sayıların adedini ve toplamını ekrana yazdıran program

a = [4,8,3,1,18,9,21,20,5,17]
n = len(a)
tekList = []
tek=0
toplam=0

for i in range(n):
    if a[i]%2 != 0:
        tek +=1
        tekList.append(a[i])
        toplam += int(a[i])
        
print("Tek sayıların;\nAdedi: {}\nlistesi: {}\nToplamı: {}".format(tek,tekList,toplam))