n=int(input())

flag=True
while n<9999:
    n+=1
    n1=n//100
    n2=n%100
    if n==(n1+n2)**2:
        print(n)
        flag=False
        break

if flag:
    print("-1")