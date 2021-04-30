x=float(input('請輸入路程公里數'))
if x>1.5:
    z=75+5*((x-1.5)//0.25)+5
else:
    z=75
print(z)        
