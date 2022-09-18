# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [3차] 방금그곡
# replace를 이용한 문자열 치환, map을 이용한 자료형 계산, slicing을 이용하여 전체적인 조건에 맞는 문자열 잘라내기, 지속적인 데이터 확인을 위해 필요한 데이터는 하나로 그룹화하여 이용

def solution(m, musicinfos):
    answer = None
    
    # 찾는 멜로디 역시 '#' 처리
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    # 멜로디 분석
    for musicinfo in musicinfos:
        start, end, name, melody = musicinfo.split(',')
        
        # 걸리는 시간(분) 구하기
        [hour1, minute1], [hour2, minute2] = map(int, start.split(':')), map(int, end.split(':'))
        minutes = (hour2-hour1)*60 + (minute2-minute1)
    
        # 전체적인 멜로디의 길이 구하기
        # 우선 '#'을 해당 부분으로 변환
        melody = melody.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        
        # 반복되는 시간대로 확인
        melody *= (minutes // len(melody) + 1)
        melody = melody[:minutes]
    
        # 원하는 멜로디 찾기
        if m not in melody:
            continue
        elif answer == None or answer[0] < minutes or (answer[0] == minutes and answer[1] > hour1+minute1):
            answer = [minutes, hour1+minute1, name]

    # 결국 하나도 안나오는 경우 "(None)"을 출력
    if answer == None:
        return "(None)"
    
    return answer[-1]

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))        # 	"HELLO"
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))        # 	"FOO"
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))       # 	"WORLD"