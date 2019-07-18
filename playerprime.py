n,m=map(int,input().split())
count=0
for i in range(n,m+1):
 p=0
 for j in range(1,i+1):
  if(i%j==0):
   p=p+1
  else :
   continue
 if(p==2):
  count=count+1
 else :
  continue
print(count)  
  
 
