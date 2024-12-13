from collections import deque


n,m=map(int, input().split())
a=[[] for _ in range(n+1)] # 인접 리스트
indeg=[0]*(n+1) # 진입 차수 리스트

for i in range(m): # 엣지 초기화
    s,e=map(int, input().split())
    a[s].append(e) # 인접 리스트
    indeg[e]+=1 # 진입 차수 저장

q=deque()

for i in range(1, n+1):
    if indeg[i]==0: # 진입 0인 것
        q.append(i) # q에 넣넣
    
while q:
    now=q.popleft()
    print(now, end=' ')
    for next in a[now]:
        indeg[next]-=1
        if indeg[next]==0:
            q.append(next)