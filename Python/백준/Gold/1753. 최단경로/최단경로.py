import sys
from queue import PriorityQueue
input=sys.stdin.readline

v,e=map(int, input().split())
k=int(input())
dist=[sys.maxsize]*(v+1) # 가중치
vis=[False]*(v+1) # 방문 배열
a=[[] for _ in range(v+1)] # 인접
q=PriorityQueue()

for _ in range(e):
    s,E,w=map(int, input().split())
    a[s].append((E,w))

q.put((0,k)) # 시작점
dist[k]=0

while q.qsize()>0:
    arr=q.get()
    now=arr[1]
    if not vis[now]:
        vis[now]=True
        for tmp in a[now]:
            next=tmp[0]
            value=tmp[1]
            if dist[next]>dist[now]+value:
                dist[next]=dist[now]+value
                q.put((dist[next], next))

for i in range(1,v+1):
    if vis[i]:
        print(dist[i])
    else: print("INF")