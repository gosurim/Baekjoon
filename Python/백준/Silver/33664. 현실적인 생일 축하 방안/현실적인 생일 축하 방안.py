b,n,m=map(int, input().split())
arr=[input().split() for _ in range(n)]
arr1=[input() for _ in range(m)]

tot=0
for i in range(n):
    if arr[i][0] in arr1:
        tot+=int(arr[i][1])

print("acceptable" if tot<=b else "unacceptable")