# Dizinin ortalamasına en yakın dizi elemanını 
# bulan program

a = [4, 8, -4, 18, 9, 21, 20, 5, -17,-1]
# a = [4, 8, -4, 18, 9, 21, -200, 5,5,10,23,95,63,-86 -17,-1]
n = len(a)
sum = 0

for i in range(n):
    sum += a[i] #63
average = sum / n #6.3

print(sum)
print(average)

temp = 1000000000
for i in range(n):
    distance = abs(average - a[i])
    if temp > distance:
        temp = distance
        miniDistance = a[i]

print(miniDistance)


