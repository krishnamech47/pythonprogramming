n=int(input())
a=list(map(int,input().split()))[:n]
b=0
c=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if((a[i]==a[j]) and (a[i] not in c)):
            c.append(a[i])
            b=b+1 
if(len(c)==0):
    print("unique")
for k in range(0,len(c)):
        print(c[k],end=" ")
    
