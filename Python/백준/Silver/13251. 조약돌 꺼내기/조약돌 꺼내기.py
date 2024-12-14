d=[0]*51
pro=[0]*51 # 확률 저장 리스트 
m=int(input())
d=list(map(int, input().split()))
t=0

for i in range(m):
    t+=d[i]

k=int(input())
ans=0

for i in range(m):
    if d[i]>=k:
        pro[i]=1 # 초기화 
        for x in range(k):
            pro[i]=pro[i]*(d[i]-x)/(t-x)
        ans+=pro[i]

print(ans)