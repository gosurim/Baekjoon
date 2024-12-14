from queue import PriorityQueue
n=int(input())
pq=PriorityQueue()
mq=PriorityQueue()
one=0
zero=0

for i in range(n):
    x=int(input())
    if x>1:
        pq.put(x*-1)
    elif x==1:
        one+=1
    elif x==0:
        zero+=1
    else:
        mq.put(x)

sum=0

while pq.qsize()>1: # 양수 처리
    x1=pq.get()*-1
    x2=pq.get()*-1
    sum+=x1*x2

if pq.qsize()>0:
    sum+=pq.get()*-1

while mq.qsize()>1:
    x1=mq.get()
    x2=mq.get()
    sum+=x1*x2

if mq.qsize()>0:
    if zero==0:
        sum+=mq.get()

sum+=one
print(sum)