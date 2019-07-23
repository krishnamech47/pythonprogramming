n=int(input())
a=list(map(int,input().split()))[:n]
b=0
c=[]
for i in range (0,len(a)):
    if(a[i]==i):
        c.append(a[i])
if(len(c)==0):
    print("-1")
for j in range(0,len(c)):
    print(c[j],end=" ")
