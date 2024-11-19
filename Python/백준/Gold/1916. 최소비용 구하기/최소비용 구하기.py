from queue import PriorityQueue
import sys


n=int(input())
m=int(input())
arr=[[] for _ in range(n+1)]
dist=[sys.maxsize]*(n+1)
vis=[False]*(n+1)

for _ in range(m):
    s,e,w=map(int, input().split())
    arr[s].append((e,w))

s,e=map(int, input().split())

def dijkstra(s,e):
    pq=PriorityQueue()
    pq.put((0,s))
    dist[s]=0
    while pq.qsize()>0:
        nowNode=pq.get()
        now=nowNode[1]
        if not vis[now]:
            vis[now]=True
            for x in arr[now]:
                if not vis[x[0]] and dist[x[0]] > dist[now] + x[1]:
                    dist[x[0]]=dist[now]+x[1]
                    pq.put((dist[x[0]], x[0]))
    return dist[e]

print(dijkstra(s,e))