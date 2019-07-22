n=int(input())
n1=1
n2=0
c=0
while(c<n):
    print(n1,end=" ")
    nth=n1+n2
    n2=n1
    n1=nth
    c=c+1
