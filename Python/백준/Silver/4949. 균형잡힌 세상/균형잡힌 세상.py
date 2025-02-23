import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == ".":  # 종료 조건
        break

    st = []  # ✅ 스택을 매 줄마다 초기화
    balanced = True  # ✅ 균형 여부 추적

    for i in n:
        if i in "([":  # ✅ 여는 괄호 스택에 추가
            st.append(i)
        elif i == ")":  # ✅ 닫는 소괄호 처리
            if not st or st[-1] != "(":  # 매칭되는 여는 괄호가 없으면 불균형
                balanced = False
                break
            st.pop()
        elif i == "]":  # ✅ 닫는 대괄호 처리
            if not st or st[-1] != "[":  # 매칭되는 여는 괄호가 없으면 불균형
                balanced = False
                break
            st.pop()

    # ✅ 최종적으로 스택이 비어 있으면 "yes", 아니면 "no" 출력
    if balanced and not st:
        print("yes")
    else:
        print("no")
