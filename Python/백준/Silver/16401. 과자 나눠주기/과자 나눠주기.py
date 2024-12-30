n,m=map(int, input().split())
A=list(map(int, input().split()))

s, e=1, int(1e9)
rslt=0

while s<=e:
    mid=(s+e)//2
    cnt=0
    for i in A:
        cnt+=i//mid
    if cnt>=n:
        rslt=max(rslt, mid)
        s=mid+1
    else:
        e=mid-1
print(rslt)