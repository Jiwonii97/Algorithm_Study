# 코딩테스트 연습 / 연습문제 / 2016년

def solution(a, b):
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month = [31, 29, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
    days = b-1
    for idx in range(a-1):
        days += month[idx]
    
    return day[days%7]

'''
    < 다른 풀이 >
    # 단순 수학 구현 문제
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
'''