a = [-1, 4, 6, 7, 12, 15, 16, 26, 27, 34]
sizeA = len(a) #10
b = [3, 5, 9, 20, 23, 30, 37, 97, 98, 99,123]
sizeB = len(b) #10
c = (sizeA+sizeB) * [None]
sizeC = len(c) #20


i = 0; j = 0; k = 0

while k < sizeC:

    if i == sizeA or a[i] > b[j]:
        c[k] = b[j]
        j += 1
    elif j == sizeB or a[i] < b[j]:
        c[k] = a[i]
        i += 1
    k += 1

print(c)