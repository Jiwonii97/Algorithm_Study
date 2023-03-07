# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [3차] 파일명 정렬
# 정규식 활용 (re.split() : 해당 정규식을 기준으로 문자열 분리)

import re


def solution(files):
    subfile = [re.split('([0-9]+)', file) for file in files]

    subfile.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(x) for x in subfile]

    return answer


print(solution(["img12.png", "img10.png", "img02.png",
      "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress",
      "A-10 Thunderbolt II", "F-14 Tomcat"]))

'''
    < 처음 풀이 >
    # 하나씩 확인하며 일일이 slicing 진행하고 정렬로 결과 출력, sol 실패
    def solution(files):
        subfile = []
        head, body, tail = "", "", ""
        
        for file in files:
            # Head 찾기 : 문자열 부분 확인
            for idx in range(len(file)):
                if file[idx].isalpha() or file[idx] in [" ", ".", "-"]:
                    continue
                else:
                    head = file[:idx]
                    file = file[idx:]
                    break
                
            # Body 찾기
            for idx in range(len(file)):
                if file[idx].isdigit():
                    continue
                else:
                    body = file[:idx]
                    tail = file[idx:]
                    break
            subfile.append([head, body, tail])
        
        subfile.sort(key=lambda x: (x[0].lower(), int(x[1])))
        answer = [''.join(x) for x in subfile]
        
        return answer
        
    < 다른 풀이 >
    # 일일이 접근하는게 아니라 정규식으로 head와 body부분을 추려내서 key로 정렬 진행
    
    import re
    def solution(files):
        a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
        b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
        return b
'''
