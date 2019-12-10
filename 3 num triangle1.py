import math
a,b,c = [int(x) for x in input().split()]
if a+b <= c or a+c <= b or b+c <= a :
    res = 'no'
elif a==b or a==c or b==c :
    res = 'no'
else :
    res = 'yes'
print(res,end='')
