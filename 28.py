x="1234"
y=-1
play = True
data=[5621, 4321, 1324 ,1234 ,0000]
index=0
y = input()

while play  and y !=0 and y!='0000':
    z = list(y)
    a = 0
    for i in range(4):
        if (x[i] == z[i]):
            a = a + 1
    b = 0
    j = 0
    while j < 4:
        k = 0
        while k < 4:
            if j == k:
                k = k + 1
                continue
            if (x[j] == z[k]):
                b = b + 1
            k = k + 1
        j = j + 1


    print(a, "A", b, "B")
    y = input()