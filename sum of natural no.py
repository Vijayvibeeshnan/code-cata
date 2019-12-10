K=int(input())
if K < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(K > 0):
       sum += K
       K -= 1
   print(sum)
