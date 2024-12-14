import sys
input=sys.stdin.readline
n=int(input()) # 도시 수
w=[]

for i in range(n):
    w.append([])
    w[i]=list(map(int, input().split()))

d=[[0 for _ in range(1<<16)] for i in range(16)]

def tsp(c,v): # 완전 탐색의 형태로 수행
    if v==(1<<n)-1: # 모든 노드 방문했을 때
        if w[c][0]==0:
            return float('inf')
        else:
            return w[c][0]
    if d[c][v]!=0: 
        return d[c][v]
    mi=float('inf')
    for i in range(n):
        # vis x, 갈 수 있는 도시
        if (v& (1<<i)) == 0 and w[c][i] !=0:
            mi=min(mi, tsp(i, (v|(1<<i)) ) + w[c][i] )
    d[c][v]=mi
    return d[c][v]

print(tsp(0,1))

