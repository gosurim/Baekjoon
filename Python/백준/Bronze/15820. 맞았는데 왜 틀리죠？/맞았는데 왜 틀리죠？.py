s, ss=map(int, input().split())
flag1=True
flag2=True

for _ in range(s):
    a,b=map(int ,input().split())
    if a!=b:
        flag1=False
for _ in range(ss):
    a,b=map(int ,input().split())
    if a!=b:
        flag2=False

if flag1 and flag2:
    print("Accepted")
elif not flag1:
    print("Wrong Answer")
else: print("Why Wrong!!!")
    