n=int(input())
cnt=0
flag=False
for i in range(1,n):
    cnt=i
    x=str(i)
    for j in x:
        cnt+=int(j)
    if cnt==n:
        flag=True
        print(i)
        break

if not flag :
    print(0)

