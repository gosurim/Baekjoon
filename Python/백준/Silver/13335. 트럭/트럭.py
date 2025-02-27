import sys

n, w, l = map(int, input().split())
q = list(map(int, input().split()))
 
dis=[0]*w # 다리길이
time=0
while dis:
    time +=1
    dis.pop(0)
    if q:
        if sum(dis)+q[0]<=l: # 하중 이하
            dis.append(q.pop(0))
        else:
            dis.append(0) # 아니면 빈 공간

print(time)