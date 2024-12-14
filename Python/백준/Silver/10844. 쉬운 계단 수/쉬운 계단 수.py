import sys
input=sys.stdin.readline
mod=10**9
n=int(input())
d=[[0 for _ in range(11)] for _ in range(n+1)]

for i in range(1,10):
    d[1][i]=1

for i in range(2,n+1):
    d[i][0]=d[i-1][1]
    d[i][9]=d[i-1][8]
    for j in range(1,9):
        d[i][j]=(d[i-1][j-1]+d[i-1][j+1])%mod

sum=0

for i in range(10):
    sum=(sum+d[n][i]) %mod

print(sum)