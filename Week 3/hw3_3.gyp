# 1 ile 100 arasındaki 3'ün 4'ün ve 5'in katlarını
# tekrar olmadan ekrana
# iç içe yazdıran program


for i in range(1,100):
    if i%3 == 0:
        print(i)
    elif i%4 == 0:
        print("\t",i)
    elif i%5 == 0:
        print("\t\t",i)