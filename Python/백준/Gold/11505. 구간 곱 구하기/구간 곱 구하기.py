import sys
input = sys.stdin.readline
sys.stdout.write

n, m, k = map(int, input().split())
mod = 1000000007

# 트리 크기 계산
h = 0
leaf = n
while leaf != 0:
    leaf //= 2
    h += 1
tsize = 2 ** (h + 1)
left = tsize // 2 - 1
a = [1] * (tsize + 1)

# 리프 노드 입력
for i in range(left + 1, left + 1 + n):
    a[i] = int(input())

# 세그먼트 트리 생성
def Tree(i):
    while i != 1:
        a[i // 2] = a[i // 2] * a[i] % mod
        i -= 1

Tree(tsize - 1)

# 값 변경 함수
def changeVal(ind, val):
    a[ind] = val
    while ind > 1:
        ind //= 2
        a[ind] = a[ind * 2] % mod * a[ind * 2 + 1] % mod

# 구간 곱 계산 함수
def getmul(s, e):
    mul = 1
    while s <= e:
        if s % 2 == 1:
            mul = mul * a[s] % mod
            s += 1
        if e % 2 == 0:
            mul = mul * a[e] % mod
            e -= 1
        s //= 2
        e //= 2
    return mul

# 명령 처리
output = []
for _ in range(m + k):
    q, s, e = map(int, input().split())
    if q == 1:
        changeVal(left + s, e)
    elif q == 2:
        s += left
        e += left
        output.append(getmul(s, e))

# 결과 출력
sys.stdout.write("\n".join(map(str, output)) + "\n")
