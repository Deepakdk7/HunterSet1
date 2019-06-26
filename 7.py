ax=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(0,ax):
    if a[i]%2!=0 and i%2==0:
        c.append(a[i])
    elif a[i]%2==0 and i%2!=0:
        c.append(a[i])
print(*c)
