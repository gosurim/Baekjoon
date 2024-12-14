rslt=0
a=list(map(str, input().split("-")))
# +끼리 묶임.
def func(i):
    sum=0
    temp=str(i).split("+") # 묶인 것을 또 해체
    for i in temp:
        sum+=int(i)
    return sum

for i in range(len(a)):
    temp=func(a[i])
    if i==0:
        rslt+=temp # 가장 앞에 있는 건 더해주고
    else: 
        rslt-=temp # 그 뒤부터 빼주기
print(rslt)