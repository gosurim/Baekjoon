import sys
input=sys.stdin.readline
d=[[0 for _ in range(1001)] for _ in range(1001)]
n,m=map(int, input().split())
max=0

for i in range(n):
    num=list(input())
    for j in range(m):
        d[i][j]=int(num[j])
        if d[i][j]==1 and j>0 and i>0:
            d[i][j]=min(d[i-1][j-1], d[i-1][j], d[i][j-1]) +d[i][j]
        if max<d[i][j]:
           max=d[i][j] 

print(max*max)