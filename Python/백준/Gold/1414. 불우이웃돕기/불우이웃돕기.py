import sys
input=sys.stdin.readline
from queue import PriorityQueue
n=int(input())
q=PriorityQueue()

sum=0
for i in range(n):
    a=list(input())
    for j in range(n):
        w=0
        if 'a'<=a[j]<='z': w=ord(a[j])-ord('a')+1
        elif 'A'<=a[j]<='Z': w=ord(a[j])-ord('A')+27
        sum+=w
        if i!=j and w!=0:
            q.put((w, i, j))

parent=[0]*(n)
for i in range(n):
    parent[i]=i
def find(a):
    if a==parent[a]:return a
    else: 
        parent[a]=find(parent[a])
        return parent[a]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

rslt=0
usee=0
while q.qsize()>0:
    w,s,e=q.get()
    if find(s) != find(e):
        union(s,e)
        rslt+=w
        usee+=1

if usee==n-1:
    print(sum-rslt)
else:
    print(-1)