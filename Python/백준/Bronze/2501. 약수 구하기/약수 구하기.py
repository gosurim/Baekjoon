n, k = map(int, input().split())

cnt = 0
for i in range(1, n + 1):
    if n % i == 0:  # i가 n의 약수인지 확인
        cnt += 1
        if cnt == k:  # K번째 약수이면 출력 후 종료
            print(i)
            break
else:
    print(0)  # K번째 약수가 없을 경우
