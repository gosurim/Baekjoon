n=int(input())
cnt=0
i=5

while n//i>0:
    cnt+=n//i
    i*=5

print(cnt)