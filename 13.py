s = input('請輸入一字元為：')
if not s:
    print('請不要輸入空白字串！')
    s = input('請重新輸入：')

a = len(s)
i = 0
count = 1    
while i <= (a/2):
    if s[i] == s[a-i-1]:
        count = 1
        i += 1
    else:
        count = 0
        break

if count == 1:
    print('yes')
else:
    print('no')
