from collections import deque

n,m=map(int, input().split())
q=deque([i for i in range(1,n+1)])
rslt=[]

while q:
    for _ in range(m-1):
        q.append(q.popleft()) 
        # 왼쪽에 있던 것을 뒤로 옮겨준다.
    rslt.append(str(q.popleft())) # 출력
    
print('<'+', '.join(rslt)+'>')