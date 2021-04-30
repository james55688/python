x=int(input("X軸座標"))
y=int(input("Y軸座標"))
z=x*x+y*y
if x>0 and y>0:
    print('該點位在第一象限，離遠點距離為根號%d'%z)
elif x<0 and y>0:
    print('該點位在第二象限，離遠點距離為根號%d'%z)
elif x<0 and y<0:
    print('該點位在第三象限，離遠點距離為根號%d'%z)
elif x>0 and y<0:
    print('該點位在第四象限，離遠點距離為根號%d'%z)
elif x<0 and y==0:
    print('該點位在左半平面X軸上，離遠點距離為根號%d'%z)
elif x>0 and y==0:
    print('該點位在右半平面X軸上，離遠點距離為根號%d'%z)
elif x==0 and y>0:
    print('該點位在上半平面Y軸上，離遠點距離為根號%d'%z)
elif x==0 and y<0:
    print('該點位在下半平面Y軸上，離遠點距離為根號%d'%z)       
else:
    print('該點位於原點')    



