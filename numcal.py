n=input()
m=len(n)
count=0
for i in range (0,m):
    if(n[i]=="1" or n[i]=="2" or n[i]=="3" or n[i]=="4" or n[i]=="5" or n[i]=="6" or n[i]=="7" or n[i]=="8" or n[i]=="9" or n[i]=="0"):
        count=count+1
    else :
        continue
print(count)
