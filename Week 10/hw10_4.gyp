# b dizisindeki elemanların tamamının a dizisinde
# olup olmadığını ekrana yazdıran program

a = [4, 8, 3, 1, 18, 9, 21, 20, 5, 17]
b = [9, 5, 1, 8, 100]
sizeA = len(a)
sizeB = len(b)

counter = 0

for i in range(sizeB):
    for j in range(sizeA):
        if b[i] == a[j]:
            counter += 1


if counter == sizeB:
    print("OK")
else:
    print("NO")

