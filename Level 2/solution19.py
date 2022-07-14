# 코딩테스트 연습 / 깊이/너비 우선 탐색(DFS/BFS) / 타겟 넘버
# 전역변수와 재귀를 활용한 DFS 문제

answer = 0

def cal_number(total_num, numbers, idx, target):
    global answer    
    # 조건 미달 (차가 타겟넘버 보다 작아지거나, 마지막 인덱스까지 넘어간 경우)
    if idx == len(numbers):
        # 조건 만족
        if total_num == target:
            answer += 1
        return
    cal_number(total_num+numbers[idx],numbers,idx+1, target)
    cal_number(total_num-numbers[idx],numbers,idx+1, target)
    return

def solution(numbers, target):
    global answer
    answer = 0
    cal_number(0, numbers, 0, target)
    return answer

print(solution([1, 1, 1, 1, 1],3))
print(solution([4, 1, 2, 1],4))

'''
    < 다른 풀이 >
    # 타겟이 원하는 값이 나올때만 값을 더함
    def solution(numbers, target):
        if not numbers and target == 0 :
            return 1
        elif not numbers:
            return 0
        else:
            return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''