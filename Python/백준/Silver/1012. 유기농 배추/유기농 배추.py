# 구간 cnt
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(r,c):
    q=deque()
    q.append([r,c])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
                arr[nx][ny]=0
                q.append([nx,ny])

for _ in range(int(input())):
    n,m,k=map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for i in range(k):
        a,b=map(int, input().split())
        arr[a][b]=1

    cnt=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                cnt+=1
                arr[i][j]=0
                dfs(i,j)
    print(cnt)