st=[]
for _ in range(int(input())):
    n=int(input())
    if n==0:
        st.pop()
    else:
        st.append(n)

print(sum(st))