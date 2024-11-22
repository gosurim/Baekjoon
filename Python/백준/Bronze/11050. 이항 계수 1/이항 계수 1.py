n,k=map(int, input().split())
rslt=1
for i in range(k):
    rslt*=n
    n-=1

div=1
for i in range(2, k+1):
    div*=i

print(rslt//div)