str=list(input())
n=len(str)
for k in range(0,n,2):
  str[k],str[k+1]=str[k+1],str[k]
print(*str,sep="")
