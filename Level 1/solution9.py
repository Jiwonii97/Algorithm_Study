# 코딩테스트 연습 / 월간 코드 챌린지 시즌2 / 음양 더하기

true = 1
false = 0

def solution(absolutes, signs):
    answer = 0
    for num1, num2 in zip(absolutes, signs):
        answer += num1*pow(-1,1-num2)
    return answer


print(solution([4,7,12],[true,false,true]))
print(solution([1,2,3],[false,false,true]))

'''
< 다른 풀이 >
# zip과 list comprehension 사용
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
'''