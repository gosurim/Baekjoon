import sys
input=sys.stdin.readline
n,m=map(int, input().split())
h=0
leaf=n

while leaf!=0:
    leaf//=2
    h+=1

tsize=pow(2, h+1)
left=tsize//2-1
tree=[sys.maxsize]*(tsize+1)

for i in range(left+1, left+1+n):
    tree[i]=int(input())

def Tree(i): # 인덱스 트리 생성
    while i!=1:
        if tree[i//2]>tree[i]:
            tree[i//2]=tree[i]
        i-=1

Tree(tsize-1)

def getmi(s,e):
    mi=sys.maxsize
    while s<=e:
        if s%2==1:
            mi=min(mi, tree[s])
            s+=1
        if e%2==0:
            mi=min(mi, tree[e])
            e-=1
        s//=2
        e//=2
    return mi

for _ in range(m):
    s,e=map(int, input().split())
    s+=left
    e+=left
    print(getmi(s,e))
