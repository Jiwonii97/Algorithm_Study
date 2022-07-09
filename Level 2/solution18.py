# 코딩테스트 연습 / 완전탐색 / 카펫
# xy = yellow, (x+2)*(y+2)-xy = brown
# 넓이 이용

def solution(brown, yellow):
    answer = 1
    
    # 탐색 진행
    while answer <= yellow:
        if yellow%answer == 0:
            width, height = int(yellow/answer), answer
            
            # (x+2)(y+2) = brown + yellow
            if (width+2)*(height+2) == (brown+yellow):
                break
        
        answer += 1
        
    return [width+2, height+2]

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))

'''
    < 다른 풀이 > - 둘레의 길이 이용
    def solution(brown, red):
        for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
'''