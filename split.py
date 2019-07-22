n=int(input())
a=list(map(int,input().split()))[:n]
for i in range (0,n):
 print(a[i],end=" ")
 print(i)
