import sys
input=sys.stdin.readline
n,m,k=map(int, input().split())
h=0 # 높이
lef=n # 리프 노드

while lef!=0: # tree 높이 구하기
    lef//=2
    h += 1

tsize=pow(2, h+1) 
left=tsize//2-1 # 리프노드 시작 인덱스
tree=[0]*(tsize+1)

for i in range(left+1, left+1+n): # 리프노드 채우기
    tree[i]=int(input())

def Tree(i):
    while i!=1:
        tree[i//2]+=tree[i] # 부모노드에 덧덧
        i-=1

Tree(tsize-1) # 끝에서부터 들어감

def changeVal(sind, val): 
    diff=val-tree[sind] # 현재 노드값과 변경된 값 차이
    while sind>0:
        tree[sind]=tree[sind]+diff
        sind=sind//2

def getSum(s,e):
    sum=0
    while s<=e:
        if s%2==1:
            sum+=tree[s]
            s+=1
        if e%2==0:
            sum+=tree[e]
            e-=1
        s=s//2
        e=e//2
    return sum

for _ in range(m+k):
    que, s, e=map(int, input().split())
    if que==1:
        changeVal(left+s, e)
    elif que==2:
        s=s+left
        e=e+left
        print(getSum(s,e))