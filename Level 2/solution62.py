# 코딩테스트 연습 / 월간 코드 챌린지 시즌2 / 2개 이하로 다른 비트
# 짝/홀수의 경우의 수를 나눠 연산 진행, 원하는 값을 만들어냄, XOR로 접근방식은 좋았으나 시간초과 문제 발생
# 짝수의 경우 1을 더하면 다른 비트가 1개 이므로 조건을 만족한다.
# 홀수의 경우 0의 위치를 찾아 이의 위치를 조정하면 원하는 값을 찾을 수 있음

def solution(numbers):
    answer = []
    
    for number in numbers:
        
        # 만약 짝수라면 1을 더하고 return
        if number % 2 == 0: answer.append(number+1)
        else:
            tmp = '0'+bin(number)[2:]
            idx = tmp.rfind('0')
            tmp = tmp[:idx]+'10'+tmp[idx+2:]
            answer.append(int(tmp,2))
    
    return answer

print(solution([2,7,11]))     # [3,11]

'''
    < 처음 풀이 >
    # XOR를 사용하여 비트연산으로 구하려고 하였으나 최대값이 10^15인 입장에서 시간초과가 발생
    
    for target in range(number+1,10**15+1):
        tmp = target ^ number       # XOR을 사용해서 같은 숫자가 있는지 따로 확인 (같으면 0, 다르면 1)
        if 0< bin(tmp).count('1') <=2:
            break
        target += 1
    answer.append(target)

    < 다른 풀이 >
    def solution(numbers):
        answer = []
        for idx, val in enumerate(numbers):
            answer.append(((val ^ (val+1)) >> 2) +val +1)

        return answer
'''