from queue import PriorityQueue
import sys
input=sys.stdin.readline

n,m=map(int, input().split())
parent=[i for i in range(n+1)]
def find(a):
    if a==parent[a]: return a
    else:
        parent[a]=find(parent[a])
        return parent[a]
def union(a,b):
    if find(a)!=find(b):
        parent[find(b)]=find(a)
def check(a,b):
    return find(a)==find(b)

q=PriorityQueue()
for _ in range(m):
    a,b,w=map(int, input().split())
    q.put((w, a,b))
   
rslt=0
last=0
while q.qsize()>0:
    w,a,b=q.get()
    if not check(a,b):
        union(a,b)
        rslt+=w
        last=w # qp 때문에 가중치 가장 큰 것임
print(rslt-last)