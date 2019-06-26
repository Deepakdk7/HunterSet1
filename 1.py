ax=int(input())
a=input().split()
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    if a.count(i)>1:
        c.append(i)
c.sort()
print(*c)
