# 문해프 70번
import sys
input=sys.stdin.readline
n=int(input())
tree={} # 딕셔너리

for _ in range(n):
    root, left, right=input().split()
    tree[root]=[left, right]

def preo(now):
    if now=='.':
        return
    print(now, end='') # 현재 출려
    preo(tree[now][0])  # 왼쪽
    preo(tree[now][1])  # 오른쪽

def ino(now):
    if now=='.':
        return
    ino(tree[now][0])
    print(now, end='')
    ino(tree[now][1])

def poso(now):
    if now=='.':
        return
    poso(tree[now][0])
    poso(tree[now][1])
    print(now, end='')

preo('A')
print()
ino('A')
print()
poso('A')