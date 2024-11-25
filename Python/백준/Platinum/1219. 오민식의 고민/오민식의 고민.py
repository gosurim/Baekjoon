import sys


input=sys.stdin.readline
n,sCity, eCity, m=map(int, input().split())
edges=[]
distance=[-sys.maxsize]*n

for _ in range(m):
    s,e,price=map(int, input().split())
    edges.append((s,e,price))

cityMoney=list(map(int, input().split()))

distance[sCity]=cityMoney[sCity]

for i in range(n+101):
    for s, e, price in edges:
        if distance[s] == -sys.maxsize:
            continue
        elif distance[s] == sys.maxsize:
            distance[e]=sys.maxsize
        elif distance[e] < distance[s] +cityMoney[e]-price:
            distance[e] = distance[s] +cityMoney[e] - price
            if i>=n-1:
                distance[e] = sys.maxsize
            
if distance[eCity]==-sys.maxsize:
    print("gg")
elif distance[eCity]== sys.maxsize:
    print("Gee")
else:
    print(distance[eCity])