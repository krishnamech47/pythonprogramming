n,p=map(int,input().split())
for i in range(n,p+1):
 p=0
 for j in range(1,i+1):
  if i%j==0 :
   p=p+1
  else :
   continue
 if(p==2):
  print(i,end=" ")
 else :
  continue
 

