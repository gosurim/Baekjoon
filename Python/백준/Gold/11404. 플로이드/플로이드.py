import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
dis=[[sys.maxsize for j in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    dis[i][i]=0

for i in range(m):
    s,e,v=map(int, input().split())
    if dis[s][e]>v:
        dis[s][e]=v

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dis[i][j]>dis[i][k]+dis[k][j]:
                dis[i][j]=dis[i][k]+dis[k][j]

for i in range(1, n+1):
    for j in range(1,n+1):
        if dis[i][j]==sys.maxsize:
            print(0, end=' ')
        else:
            print(dis[i][j], end=' ')
    print()