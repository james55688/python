a,b = map(float,input("輸入質").split(','))
if a==186:
    if b>186:
        x=b*0.09*0.8
    else:
        x=b*0.09*0.9
elif a==386:
    if b>386:
        x=b*0.08*0.7
    else:
        x=b*0.09*0.8
elif a==586:
    if b>586:
        x=b*0.07*0.6
    else:
        x=b*0.09*0.7
elif a==986:
    if b>986:
        x=b*0.06*0.5
    else:
        x=b*0.09*0.6        
else:
    print('錯誤')
print('通話費為%f'%x)    
