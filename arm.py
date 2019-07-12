import math as m
n=int(input())
temp=n
arm=n
p=0
sum=0
rem=0
while n>0 :
 n=n/10
 p=p+1
while temp>0 :
 rem=temp%10
 sum=sum+m.pow(rem,p)
 temp=temp/10
if arm==sum :
 print("yes")
else :
 print("no")
 
