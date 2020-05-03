# En büyük negatif tam sayıyı bulan program

a = [-1,4, 8, -4, 18, 9, 21, 20, 5, -17,5]
n = len(a)
maxNeg = -999
for i in range(n):
    if a[i] < 0:
        if maxNeg < a[i]:
            maxNeg = a[i]
print(maxNeg)
