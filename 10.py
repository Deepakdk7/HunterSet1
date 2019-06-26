ax=input().split()
a=input().split()
b=input().split()
a.sort()
b.sort()
c=0
for i in b:
    if i in a:
        c=c+1
if c==len(b):
    print('YES')
else:
    print('NO')
