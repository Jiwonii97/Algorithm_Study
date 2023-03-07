# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0
    start, end = 0, 0

    while start < len(s):
        target = s[start]
        point = [1, 0]
        end = start + 1

        if end >= len(s):   # 한글자 밖에 안남은 경우
            answer += 1
            break

        for i in range(end, len(s)):
            if s[i] != target:
                point[1] += 1
            else:
                point[0] += 1

            if point[0] == point[1]:
                break
        else:
            pass

        start = i+1
        answer += 1

    return answer


print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
