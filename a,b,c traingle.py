a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if(a+b<=c)or(a+c<=b)or(b+c<=a):
    print("no")
else:
    print("yes")
