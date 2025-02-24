for _ in range(int(input())):
    st=[]
    flag=False
    n=input()
    for s in n:
        if s=="(":
            st.append(s)
        elif s==")":
            if st and st[-1]=="(":
                st.pop()
                flag=True
            else: 
                flag=False
                print("NO")
                break
    if st: print("NO")
    elif flag:
        print("YES")