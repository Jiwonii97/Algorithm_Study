# 코딩테스트 연습 / 스택/큐 / 올바른 괄호

def solution(s):
    st = []
    
    for s1 in s:
        if s1 == "(":
            st.append(s1)
        else:
            if not st and s1 == ")":
                return False            
            elif s1 == ")" and st[-1] == "(":
                st.pop()
            else:
                return False

    return True if len(st) == 0 else False

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))

'''
    < 다른 풀이 >
    # try-except를 사용해서 스택 처리
    def is_pair(s):
        st = list()
        for c in s:
            if c == '(':
                st.append(c)

            if c == ')':
                try:
                    st.pop()
                except IndexError:
                    return False

        return len(st) == 0
'''