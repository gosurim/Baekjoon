# 양방향
# dfs
n=int(input())
v=int(input())
graph=[[] for i in range(n+1)]
vis=[0]*(n+1)
for i in range(v):
    a,b=map(int, input().split())
    graph[a]+=[b] # 양방향, 인접
    graph[b]+=[a]

def dfs(v):
    vis[v]=1
    for nx in graph[v]: # 1에서 꺼내지는 것들부터
        if vis[nx]==0:
            dfs(nx)     # 재귀
dfs(1)
print(sum(vis)-1)