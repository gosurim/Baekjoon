#bfs
from collections import deque
n=int(input())
m=n
arr=[list(map(int, input().strip())) for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

danji=0
house=[]

def bfs(x,y):
    h=1
    q=deque()
    q.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
                h+=1
                arr[nx][ny]=0
                q.append([nx,ny])
    house.append(h)


for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            arr[i][j]=0
            danji+=1
            bfs(i,j)

print(danji)
house.sort()
for i in range(danji):
    print(house[i])