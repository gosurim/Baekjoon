import math
import sys
input=sys.stdin.readline
ma=1000000
sosu=[0]*(ma+1)
for i in range(2, ma+1):
    sosu[i]=i

for i in range(2, int(math.sqrt(ma))+1):
    if sosu[i]==i:
        for j in range(i*i, ma+1, i):
            sosu[j]=0

while True:
    flag=False
    n=int(input())
    if n==0:
        break
    for i in range(3, n//2+1, 2):
        if sosu[i] and sosu[n-i]:
            flag=True
            break
    if flag:
        print(f"{n} = {i} + {n-i}")
    else:
        print("Goldbach's conjecture is wrong.")
