n,m=map(int, input().split())
trueP=list(map(int, input().split())) # 진실을 아는 사람
t=trueP[0]
del trueP[0] # tp 명수 삭제
cnt=0
party=[[] for _ in range(m)] # [ [] [] ]

parent=[0]*(n+1)
for i in range(n+1):
    parent[i]=i

def find(a):
    if a==parent[a]:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a
def check(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return True
    return False

for i in range(m): # 파티 데이터 저장
    party[i]=list(map(int, input().split()))
    del party[i][0] # 명수 삭제하고 당겨짐

for i in range(m):
    firstP=party[i][0] # 첫번째 사람으로 부모 갱신
    for j in range(1, len(party[i])):
        union(firstP, party[i][j]) 

for i in range(m):
    flag=True
    firstP=party[i][0] # 부모가 첫번째 사람으로 바꼈으니
    # 첫번째 사람만 확인하면 됨
    for j in range(len(trueP)):
        if find(trueP[j])== find(firstP):
            # tp하고 부모가 일치하면 거짓말 못함
            flag=False
            break
    if flag:
        cnt+=1

print(cnt)