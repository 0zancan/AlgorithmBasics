# Dizinin en büyük 2. elemanını bulan program

a = [100, 4, 8, 3, 1, 18, 9, 199, 250, 155, 21, 255, 20, 5, 17, 99, 190]
n = len(a)

max = 0
secondMax = 0
for i in range(n):
    if a[i] > max:
        secondMax = max
        max = a[i]

print(max)
print(secondMax)


"""
a = [100,4,8,3,1,18,9,199,155,21,255,20,5,17,99,190]
n = len(a)

max = 0
secondMax = 0
for i in range(n):
    if a[i] > max:
        max = a[i]


for i in range(n):    
    if a[i] > secondMax and a[i] != max:
        secondMax = a[i]
    
print(max)
print(secondMax)

"""
