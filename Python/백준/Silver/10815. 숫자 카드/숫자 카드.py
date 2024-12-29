n=int(input())
A=list(map(int, input().split()))
m=int(input())
B=list(map(int, input().split()))

A.sort()

cnt=0
for x in B:
    s=0
    e=len(A)-1
    flag=False
    while s<=e:
        mid=(s+e)//2
        if A[mid]==x:
            flag=True
            break
        if A[mid]<x:
            s=mid+1
        elif A[mid]>x:
            e=mid-1
    if flag:
        print(1, end=" ")
    else:
        print(0, end=" ")