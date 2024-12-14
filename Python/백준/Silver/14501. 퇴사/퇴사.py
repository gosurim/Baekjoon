import sys
input=sys.stdin.readline
n=int(input())
d=[0]*(n+2)
t=[0]*(n+1) # 시간
p=[0]*(n+1) # 비용

for i in range(1, n+1):
    t[i], p[i]= map(int, input().split())

for i in range(n, 0,-1):
    if i+t[i]> n+1: # 퇴사일 오버
        d[i]=d[i+1]
    else:
        d[i]=max(d[i+1], d[i+t[i]]+p[i])

print(d[1])
    