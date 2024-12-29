from bisect import bisect_left as bl, bisect_right as rl

n=int(input())
A=list(map(int, input().split()))
m=int(input())
B=list(map(int, input().split()))

A.sort()
def find(a,x):
    lind=bl(a, x)
    rind=rl(a,x)
    return rind-lind

for x in B:
    print(find(A,x), end=" ")