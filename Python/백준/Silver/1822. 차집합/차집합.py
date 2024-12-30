n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

cnt = n
B_set = set(B)  # B를 set으로 변환하여 검색 속도를 높임

result = []
for x in A:
    if x in B_set:
        cnt -= 1
    else:
        result.append(x)

# 출력
print(cnt)
print(*result)
