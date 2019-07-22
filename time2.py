n,m=map(int,input().split())
a,b=map(int,input().split())
if(m<b):
 m=m+60
 n=n-1
print((n-a),end=" ")
print((m-b))
