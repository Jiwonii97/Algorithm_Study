# https://school.programmers.co.kr/learn/courses/30/lessons/12904

def solution(s):
    if len(s) == 1:
        return 1
    answer = 1

    for i in range(1, len(s)):
        for j in range(i):
            if s[j:i+1] == s[j:i+1][::-1]:
                answer = max(answer, i-j+1)

    return answer


print(solution("abcdcba"))      # 7
print(solution("abacde"))       # 3
print(solution("abcde"))        # 1

'''
    def longest_palindrom(s):
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                if s[j:j+i] == s[j:j+i][::-1]:
                    return i
'''
