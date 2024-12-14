n,k=map(int, input().split())
a=[0]*n

for i in range(n):
    a[i]=int(input())

cnt=0

for i in range(n-1, -1, -1):
    if a[i]<=k: # k보다 작거나 같으면 cnt
        cnt+=k//a[i]
        k%=a[i]

print(cnt)