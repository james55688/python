y=int(input("請輸入十進位的正整數"))
x=y
n=1
g=0       
while x>0:
    i=x%3
    g=g+n*i
    n*=10
    x//=3
print("%s的三進位為%d"%(y,g))
    