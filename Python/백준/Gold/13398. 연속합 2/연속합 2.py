n=int(input())
a=list(map(int, input().split()))

l=[0]*n
l[0]=a[0]
rslt=l[0]

for i in range(1,n):
    l[i]=max(a[i], l[i-1]+a[i])
    rslt=max(rslt, l[i])

r=[0]*n
r[n-1]=a[n-1]

for i in range(n-2, -1,-1):
    r[i]=max(a[i], r[i+1]+a[i])

for i in range(1, n-1):
    rslt=max(rslt, l[i-1]+r[i+1])

print(rslt)