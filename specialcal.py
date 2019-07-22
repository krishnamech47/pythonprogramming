n=input()
m=len(n)
count=0
for i in range (0,m):
    if(n[i].isdigit() or n[i].isalpha() or n[i]==" "):
        continue
    else :
        count=count+1
print(count)
