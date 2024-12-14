import sys
input=sys.stdin.readline

f=[0]*21 # 순열, 각 자리에 들어갈 수 있는 수 리스트
s=[0]*21
vis=[False]*21
n=int(input())
f[0]=1

for i in range(1, n+1): # 팩토리얼 초기화
    f[i]=f[i-1]*i

arr=list(map(int, input().split()))

if arr[0]==1: # k번째 순열 찾기
    k=arr[1]
    for i in range(1,n+1): 
        cnt=1
        for j in range(1,n+1):
            if vis[j]: # 이미 사용한 숫자는 쓰루
                continue
            if k<=cnt*f[n-i]: 
            # 주어진 k에 따라 각 자리에 들어갈 수 있는 수 찾기
                k-=(cnt-1)*f[n-i]
                s[i]=j
                vis[j]=True
                break
            cnt+=1
    for i in range(1, n+1):
        print(s[i], end=" ")
else:
    k=1
    for i in range(1, n+1):
        cnt=0
        for j in range(1, arr[i]):
            if not vis[j]:
                cnt+=1 # 미사용 숫자 개수 만큼 카운트
        k+=cnt*f[n-i]
        vis[arr[i]]=True
    print(k)