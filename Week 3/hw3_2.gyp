# 1 ile 100 arasındaki 3'ün 4'ün ve 5'in katlarını ekrana
# iç içe yazdıran program

for i in range(101):
    if i%3 == 0:
        print(i) # end=" "
    if i%4 == 0:
        print("\t",i)
    if i%5 == 0:
        print("\t\t",i)
