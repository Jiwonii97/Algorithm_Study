# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = 0
    maxNum = 8      # 8번 이상 숫자가 나오게 되면 -1 리턴
    dp = []

    if number < N:
        return -1

    for i in range(1, maxNum+1):
        answer_list = set()
        check_number = int(str(N)*i)
        answer_list.add(check_number)

        # i가 1인 경우는 조건문이 실행되지 않음
        for j in range(0, i-1):
            # j 개를 사용해서 만든 값들
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    answer_list.add(op1 - op2)
                    answer_list.add(op1 + op2)
                    answer_list.add(op1 * op2)

                    # try-except문 사용
                    try:
                        answer_list.add(op1 // op2)
                    except ZeroDivisionError:
                        pass

                    # if op2 != 0:        # 나머지 연산 확인
                    #     answer_list.add(op1 // op2)

        if number in answer_list:
            answer = i
            break

        dp.append(answer_list)

    else:
        return -1

    return answer


print(solution(5, 12))      # 4
print(solution(2, 11))      # 3
print(solution(5, 31168))      # -1
