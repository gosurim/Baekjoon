from queue import PriorityQueue
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
a=[[] for _ in range(n+1)]
dist=[sys.maxsize]*(n+1)
vis=[False]*(n+1)

for _ in range(m):
    s,e,w=map(int, input().split())
    a[s].append((e,w))

s,e=map(int, input().split())

def dij(s,e):
    q=PriorityQueue()
    q.put((0,s)) # 큐에는 w,node 순
    dist[s]=0
    while q.qsize() >0:
        node=q.get()
        now=node[1]
        if not vis[now]:
            vis[now]=True
            for x in a[now]:
                if not vis[x[0]] and dist[x[0]]>dist[now]+x[1]:
                    dist[x[0]]=dist[now]+x[1]
                    q.put((dist[x[0]], x[0]))
    return dist[e]

print(dij(s,e))