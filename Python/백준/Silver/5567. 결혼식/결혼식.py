import sys
from collections import deque
input=sys.stdin.readline
n,m=int(input()),int(input())
arr=[[0]*(n+1) for i in range(n+1)]
vis=[0 for _ in range(n+1)]

for i in range(m):
    a,b=map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(x):
    q=deque([x])
    vis[x]=1

    while q:
        fri=q.popleft()
        for i in arr[fri]:
            if not vis[i]:
                q.append(i)
                vis[i]=vis[fri]+1
                # ? 번째 친구

bfs(1)
cnt=0
for i in range(2, n+1):
    if 0<vis[i]<=3:
        cnt+=1

print(cnt)