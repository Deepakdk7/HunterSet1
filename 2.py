ax=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
if a.count(0)==ax:
    print('0')
else:
    print(*a,sep="")
