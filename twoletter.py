n,m=map(str,input().split())
e=len(n)-1
count=0
for i in range(0,len(n)):
 for j in range (0,len(n)):
  if(n[i]==m[j]):
   count=count+1
   break 
  else :
   continue
if(count==e):
 print("yes")
else :
 print("no")
