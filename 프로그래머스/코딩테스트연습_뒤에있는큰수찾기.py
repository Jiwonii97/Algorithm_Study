# 코딩테스트 연습 / 연습문제 / 뒤에 있는 큰 수 찾기

def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
