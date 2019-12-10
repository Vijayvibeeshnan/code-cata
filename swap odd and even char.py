s=input()
s=list(s)
len_=len(s)
for i in range(0,len_,2):
    s[i],s[i+1]=s[i+1],s[i]
print("".join(s))
