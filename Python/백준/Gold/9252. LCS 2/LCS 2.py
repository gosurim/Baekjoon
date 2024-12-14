import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
a=list(input())
a.pop()
b=list(input())
b.pop()

dp=[[0 for _ in range(len(b)+1)]for _ in range(len(a)+1)]
path=[]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1]==b[j-1]:
        # 같은 문자열일 때는 대각선 값+1
            dp[i][j]=dp[i-1][j-1]+1
        else:
        # 다른 값일 때는 왼 or 위
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

print(dp[len(a)][len(b)])

def lcs(r,c):
    if r==0 or c==0:
        return
    if a[r-1]==b[c-1]: # 같으면 lcs에 기록, 대각선
        path.append(a[r-1])
        lcs(r-1, c-1)
    else: # 다르면 왼쪽 or 위
        if dp[r-1][c]>dp[r][c-1]:
            lcs(r-1, c)
        else:
            lcs(r,c-1)

lcs(len(a), len(b))

for i in range(len(path) -1, -1,-1):
    print(path.pop(i), end="")
print()