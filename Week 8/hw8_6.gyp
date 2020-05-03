# a dizisindeki her sayıdan kaç tane olduğunu
# ekrana yazdıran program

a = [5,5,3,7,8,5,7,7,7,3,8,9,8,9,8,8,15,5,8,4]
n = len(a)
sum = 1

for i in range(n):
  for j in range(i+1,n):
    if a[i] == a[j]: #  and int(a[i]) != -10
      sum += 1
      a[j] = None
  if a[i] != None:
    print("{} sayısı {} kere tekrar etmekte".format(a[i], sum))
  sum = 1
