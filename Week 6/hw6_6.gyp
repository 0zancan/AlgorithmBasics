# 12-> Klavyeden girilen n'ye göre örnekteki gibi
# desen yazdırma
# n = 4, çıktı:
"""
      *
    * *
  * * *
* * * *   """

n = int(input("n: "))

for i in range(n): 
  for j in range(n):
    if (n-i-1)>j:
      print(" ", end = "")
    else:
      print("*", end = "")
  print() # döngünün çıkışına koymak gerek