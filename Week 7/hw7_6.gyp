# Dizinin ilk tek elemanını bulan program

a = [0,22,3,22,34,52,54,2332,12,12,12]
n = len(a)
i = 0
flag = True

while flag and i<n:
  if a[i]%2 != 0:
    print("Dizinin ilk tek elemanı",a[i])
    flag = False
  i+=1

if flag != False:
  print("Dizide tek eleman yok")


