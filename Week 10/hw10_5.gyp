# İki dizinin elemanlarının birbirine eşit olup
# olmadığını ekrana yazdıran program

a = [4, 8, 3, 1, 18, 9, 21, 20, 5, 17]
b = [4, 8, 3, 1, 18, 9, 21, 20, 5, 18]

sizeA = len(a)
sizeB = len(b)

counter = 0
flag = True

if sizeA != sizeB:
    print("İki dizi birbirine eşit değil!")
    flag = False

while flag:    
    for i in range(sizeB):
        for j in range(sizeA):
            if b[i] == a[j]:
                a[j] = None
                counter += 1
    print(counter)
    print(sizeB)
    if counter == sizeA:
        print("OK")
        flag = False
        break
    else:
        print("NO")
        flag = False
        break

#B'nin elemanları A da var mı diye soruyorum