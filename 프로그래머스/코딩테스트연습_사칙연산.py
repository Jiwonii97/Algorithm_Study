# https://school.programmers.co.kr/learn/courses/30/lessons/1843

# 뒤의 인덱스부터 찾아 들어와서 맞는 지금 까지 연산한 것의 최대 최소를 확인
def solution(arr):
    minmax = [0, 0]
    sum_value = 0
    for idx in range(len(arr)-1, -1, -1):
        if arr[idx] == '+':
            continue
        elif arr[idx] == '-':
            tempmin, tempmax = minmax
            minmax[0] = min(-(sum_value + tempmax), -sum_value+tempmin)
            # -(sum + max):-가 식전체에 붙는 경우, -sum+min:-가 이전 -값 앞까지만 붙는 경우
            minus_v = int(arr[idx+1])
            minmax[1] = max(-(sum_value+tempmin), -minus_v +
                            (sum_value-minus_v)+tempmax)
            # -(sum + min):-가 식전체에 붙는 경우, -v+(sum-v)+max:-가 바로 뒤의 값에만 붙는 경우
            sum_value = 0
        elif int(arr[idx]) >= 0:
            sum_value += int(arr[idx])
    minmax[1] += sum_value
    return minmax[1]


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))

'''
    # 처음 풀이법 -> 시간초과
    # bfs 활용
    def solution(arr):
        from collections import deque
        answer = []

        dq = deque()
        deque.append(dq, arr)

        while dq:
            calc = deque.popleft(dq)
            if len(calc) == 1:
                answer.append(calc[-1])
                continue

            for i in range(1, len(calc), 2):
                calc_number = eval(''.join(calc[i-1:i+2]))
                newCalc = calc[:i-1]+[str(calc_number)]+calc[i+2:]
                dq.append(newCalc)

        return max(map(int, answer))

'''
