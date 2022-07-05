# 코딩테스트 연습 / 정렬 / 가장 큰 수
# 정렬의 경우 문자열의 맨 앞부터 하나씩 정렬해 나가므로, 전체 자리수는 1000이하이므로 3자리의 정수이다 따라서 3번 반복을 시켜 1000이하의 자리수를 맞추고 정수의 크기를 비교

def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    list_ = map(str,sorted(numbers,key=lambda x:str(x)*3, reverse=True))
    return "".join(list_)

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([3, 30, 364, 35, 9]))