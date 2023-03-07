# https://school.programmers.co.kr/learn/courses/30/lessons/17678
# timestamp를 사용한다는 아이디어

def solution(n, t, m, timetable):
    # n회 t분 간격으로 m명을 태울수 있는 셔틀이 다님
    answer = 0

    timestamp = [int(time[:2])*60+int(time[3:])
                 for time in timetable]  # 시간 -> 분 change
    timestamp.sort()

    busTime = [9*60+t*i for i in range(n)]  # 버스 시간

    i = 0  # 버스에 탈 크루의 인덱스
    print(busTime, timestamp)
    for bt in busTime:  # 버스 도착 시간을 순회하면서
        cnt = 0  # 버스에 타는 크루 수
        while cnt < m and i < len(timestamp) and timestamp[i] <= bt:
            i += 1
            cnt += 1
        if cnt < m:  # 버스에 자리 남았으면 버스타임에 내가 타면 됨
            answer = bt
        else:  # 버스에 탈 자리 없으면 맨 마지막 크루보다 1분전에 도착
            answer = timestamp[i-1]-1

    return str(answer//60).zfill(2)+":"+str(answer % 60).zfill(2)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
      "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
