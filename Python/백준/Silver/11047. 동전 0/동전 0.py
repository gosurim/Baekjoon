n,k=map(int, input().split())
arr=[0]*n

for i in range(n):
    arr[i]=int(input())

cnt=0

for i in range(n-1, -1,-1):
    if arr[i]<=k:
        cnt+=int(k/arr[i])
        k%=arr[i]

print(cnt)