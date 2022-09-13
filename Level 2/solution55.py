# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / 주차 요금 계산
# 단순 구현 문제, 시간 계산을 분단위로 아예 바꾸어 계산하는게 크게 도움이 됨, 딕셔너리를 통해 데이터 관리

from math import ceil
def solution(fees, records):
    # fees = (기본시간, 기본요금, n분당 요금)
    # records = (시간, 번호, 입/출)
    answer = {}
    
    parking = {}
    for record in records:
        [time, carNumber, state] = record.split()
        
        # 입차
        if state == "IN":
            parking[carNumber]=int(time[:2])*60+int(time[3:])
        # 출차
        else:
            currentTime = int(time[:2])*60+int(time[3:])
            usingTime = currentTime - parking[carNumber]
            del parking[carNumber]
            
            # 출차 기록이 있는경우
            if carNumber in answer.keys():
                answer[carNumber] += usingTime
            else:
                answer[carNumber] = usingTime

    # 마감시간까지 주차한 차량 시간 계산
    if parking:
        for car in parking.keys():
            if car in answer.keys():
                answer[car] += ((23*60+59) - parking[car])
            else:
                answer[car] = ((23*60+59) - parking[car])
            
    carList = sorted(answer.keys())
    result = []
    for car in carList:
        time = answer[car]
        
        # 기본 시간을 지킨 경우
        if time < fees[0]:
            result.append(fees[1])
        # 기본 시간 초과
        else:
            result.append(fees[1]+ceil((time-fees[0])/fees[2])*fees[3])
            
    return result

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                                     "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))        # [14600, 34400, 5000]
print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))       # [0, 591]
print(solution([1, 461, 1, 10],["00:00 1234 IN"]))         # [14841]

'''
    < 다른 풀이 >
    from collections import defaultDict를 사용해 문제를 풀수도 있음(초기화를 하지 않아도 딕셔너리 정의 가능)
'''