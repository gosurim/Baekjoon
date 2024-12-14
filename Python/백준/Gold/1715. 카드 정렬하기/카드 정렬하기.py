from queue import PriorityQueue
n=int(input())
q=PriorityQueue()

for _ in range(n):
    data=int(input())
    q.put(data)

data1=0
data2=0
sum=0

while q.qsize()>1:
    data1=q.get()
    data2=q.get()
    temp=data1+data2
    sum+=temp
    q.put(temp)

print(sum)