# 코딩테스트 연습 / 연습문제 / 숫자 변환하기

def solution(x, y, n):
    answer = 0
    stack = set([x])      # stack 설정
    while stack:
        if y in stack:      # 조건에 만족하는 경우, 결과값 반환
            return answer
        nxt = set()
        for i in stack:
            if i+n <= y:    # x에 n을 더합니다
                nxt.add(i+n)
            if i*2 <= y:    # x에 2를 곱합니다
                nxt.add(i*2)
            if i*3 <= y:    # x에 3을 곱합니다
                nxt.add(i*3)
        stack = nxt      # update
        answer += 1

    return -1


print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))

'''
    def solution(x, y, n):
        answer = -1
        stack = [(x, 0)]

        while stack:
            tgt, cnt = stack.pop(0)
            if tgt == y:
                answer = cnt
                break
            elif tgt > y:
                continue
            stack.extend([(tgt+n, cnt+1), (tgt*2, cnt+1), (tgt*3, cnt+1)])

        return answer
'''
