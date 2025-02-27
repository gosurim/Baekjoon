n=input()
st=[]
cnt=0
for i in range(len(n)):
    if n[i]=="(":
        st.append("(")
    else:
        if n[i-1]=="(":
            st.pop()
            cnt+=len(st)
        else:
            st.pop()
            cnt+=1

print(cnt)