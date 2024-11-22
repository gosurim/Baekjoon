n=int(input())
arr=list(map(int, input().split()))
t,p=map(int, input().split())
cnt=0

for x in arr:
    cnt+=x//t
    if (x%t) !=0:
        cnt+=1
print(cnt)

print(n//p, end=" ")
print(n%p)