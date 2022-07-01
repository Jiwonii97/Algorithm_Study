# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 다트 게임
# 정규식 활용 문제

#   < 다른 풀이 >
# def solution(dartResult):
#     answer = []
#     pow_cal = {"S":1,"D":2,"T":3}
    
#     temp = list(dartResult)
#     num = ''
#     for tmp in temp:
#         if tmp.isnumeric():
#             num += tmp
#         elif tmp in ["S", "D", "T"]:
#             answer.append(int(num)**pow_cal[tmp])
#             num = ''
#         elif tmp == "*":
#             if len(answer)>=2:
#                 answer[-2] = answer[-2]*2
#                 answer[-1] = answer[-1]*2
#             else:
#                 answer[-1] = answer[-1]*2
#         elif tmp == "#":
#             answer[-1] = answer[-1]*(-1)
    
#     return sum(answer)

# '''
import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(p)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
# '''