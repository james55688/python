n=input("輸入電費度數:")
value=int(n)
summer=0.0
nonsummber=0.0
t1=0
if value>700:
    t1=value-700
    summer = t1 * 5.63 +(700-500)*4.97+ (500 - 330) * 4.39 + (330 - 120) * 3.02 + 120 * 2.1
    nonsummber = t1 * 4.5+(700-500)*4.01 + (500 - 330) * 3.61 + (330 - 120) * 2.68 + 120 * 2.1
elif   value>500 :
    t1=value-500
    summer = t1 * 4.97+(500-330)*4.39+(330-120)*3.02+120*2.1
    nonsummber = t1 * 4.01+(500-330)*3.61+(330-120)*2.68+120*2.1
elif   value>330 :
    t1=value-330
    summer = t1 * 4.39 +  (330 - 120) * 3.02 + 120 * 2.1
    nonsummber = t1 * 3.61 + (330 - 120) * 2.68 + 120 * 2.1
elif   value>120 :
    t1=value-120
    summer = t1 * 3.02+ 120 * 2.1
    nonsummber = t1 * 2.68+ 120 * 2.1
else :
    t1=value
    summer = t1 * 2.1
    nonsummber = t1 * 2.1
print("summner=%.2f"%summer)
print("Non-summner=%.2f"%nonsummber)
