import math
n, k = map(int, input().split())

p = [True] * (n + 1) 
cnt = 0

for i in range(2, n + 1):
    if p[i]: 
        for j in range(i, n + 1, i):
            if p[j]: 
                p[j] = False 
                cnt += 1 
                if cnt == k: 
                    print(j)
                    exit()
