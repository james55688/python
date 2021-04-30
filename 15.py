s=input("數字:")
data=[ ]
for i in range(len(s)):
    value=(int(s[i])+7)%10
    data.append(value)
t1=data[0]
t2=data[1]
data[0]=data[2]
data[2]=t1
data[1]=data[3]
data[3]=t2
for i in range(len(s)):
    print(data[i],end="")
