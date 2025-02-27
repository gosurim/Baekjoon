import heapq
import sys

n=int(sys.stdin.readline())
h=heapq
lh=[]
rh=[]
for i in range(n):
    num=int(sys.stdin.readline())

    if len(lh)==len(rh):
        h.heappush(lh,-num)
    else:
        h.heappush(rh, num)

    if rh and rh[0] < -lh[0]:
        lv=h.heappop(lh)
        rv=h.heappop(rh)

        h.heappush(lh, -rv)
        h.heappush(rh, -lv)

    print(-lh[0])

