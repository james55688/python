a = int(input("請輸入菱形行數："))
a=a//2+1
m = a
d = a
for i in range(1,a + 1): 
    print(" " * (m - 1),"*" * (2 * i - 1)) 
    m -= 1
    if i == a: 
        for y in range(1,a):
            print(" " * y,"*" * (2*d-3)) 
            d -= 1 
