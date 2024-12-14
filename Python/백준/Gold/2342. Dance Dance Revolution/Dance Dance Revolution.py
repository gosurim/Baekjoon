import sys
input=sys.stdin.readline
dp=[[[sys.maxsize for _ in range(5)]for _ in range(5)]for _ in range(100001)]
mp=[[0, 2, 2, 2, 2],
    [2, 1, 3, 4, 3],
    [2, 3, 1, 3, 4],
    [2, 4, 3, 1, 3],
    [2, 3, 4, 3, 1]]

s=1
dp[0][0][0]=0

arr=list(map(int, input().split()))
ind=0

while arr[ind]!=0:
    n=arr[ind]
    for i in range(5):
        if n==i: # 같은 자리는 던
            continue
        for j in range(5):
            dp[s][i][n]=min(dp[s-1][i][j]+mp[j][n], dp[s][i][n])

    for j in range(5):
        if n==j: # 같은 자리는 던
            continue
        for i in range(5):
            dp[s][n][j]=min(dp[s-1][i][j]+mp[i][n], dp[s][n][j])
    s+=1
    ind+=1

s-=1
rslt=sys.maxsize

for i in range(5):
    for j in range(5):
        rslt=min(rslt, dp[s][i][j])

print(rslt)