ax=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(0,ax):
    for j in range(i+1,ax):
        b.append([a[i],a[j]])
        c.append(a[i]+a[j])
for i in range(0,len(c)):
    if c[i]==0:
        print(*b[i])
        break
else:
    if c[i]==min(c):
        print(*b[i])
