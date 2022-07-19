# 코딩테스트 연습 / 2017 팁스타운 / 짝지어 제거하기
# Stack 활용 문제

def solution(s):
    st = []
    
    for s1 in s:
        if not st:
            st.append(s1)
        else:
            if st[-1] == s1:
                st.pop()
            else:
                st.append(s1)                

    return 1 if len(st) == 0 else 0

print(solution("baabaa"))
print(solution("cdcd"))