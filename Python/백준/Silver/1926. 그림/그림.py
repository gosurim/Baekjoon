# 경로
# dfs
from collections import deque
n,m=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
ar=[-1,1,0,0]
ac=[0,0,-1,1]

def dfs(r,c):
    arr[r][c]=0 # 방문
    w=1
    q=deque()
    q.append([r,c])
    while q:
        r,c=q.popleft()
        for i in range(4):
            nr=ar[i]+r
            nc=ac[i]+c
            if 0<= nr <n and 0<=nc<m and arr[nr][nc]==1:
                q.append([nr,nc])
                arr[nr][nc]=0
                w+=1
    return w

cnt=0 # 넓이
ans=0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1: # 1일 때 들어감
            cnt+=1
            ans=max(dfs(i,j), ans) # 넓이가 가장 넓은 것

print(cnt)
print(ans)