# 코딩테스트 연습 / 탐욕법(Greedy) / 구명보트
# 더블 포인터를 사용한 그리디 문제

def solution(people, limit):
    answer = 0
    people.sort()

    left, right = 0, len(people)-1
    
    while left <= right:
        # 정렬시킨 상태에서 양쪽의 경우를 확인하여 두명다 탈 수 있는경우, 양쪽을 다 땡기고 그렇지 않은 경우, 오른쪽 사람부터 보낸다
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        
        answer += 1
        
    return answer

print(solution([70, 50, 80, 50],100))
print(solution([70, 80, 50],100))
print(solution([60,70,30],100))

'''
    < 다른 풀이 >
    # deque를 활용한 문제 풀이
    # deque는 popleft와 pop이 둘다 가능
    # appendleft로 데이터를 넣을 수 있음
    
    from collections import deque

    def solution(people, limit):
        result = 0
        deque_people = deque(sorted(people))

        while deque_people:
            left = deque_people.popleft()
            if not deque_people:
                return result + 1
            right = deque_people.pop()
            if left + right > limit:
                deque_people.appendleft(left)
            result += 1
        return result
'''