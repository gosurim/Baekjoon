import sys
input=sys.stdin.readline
from collections import defaultdict

m,n=map(int, input().split())
uni=defaultdict(int) # 딕셔너리: 구조가 키, 우주가 값

for _ in range(m):
    planets=list(map(int, input().split()))
    sortplan=sorted(list(set(planets)))
    
    rank={sortplan[i] : i for i in range(len(sortplan))}
    vector=tuple([rank[i] for i in planets])

    uni[vector]+=1

sum=0
for i in uni.values():
    sum+=(i*(i-1))//2

print(sum)