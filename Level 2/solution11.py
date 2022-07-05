# 코딩테스트 연습 / 해시 / 전화번호 목록

def solution(phone_book):
    pb = sorted(phone_book)
    
    for idx in range(len(pb)-1):
        length_ = min(len(pb[idx]), len(pb[idx+1]))
        if pb[idx][:length_] == pb[idx+1][:length_]:
            return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
print(solution(["13","123","1235","567","88"]))

'''
    < 다른 풀이 >
    # startswith를 사용해 굳이 문자열 길이를 따로 구하지 않고도 해당 단어로 시작하는지 확인 가능
    def solution(phoneBook):
        phoneBook = sorted(phoneBook)

        for p1, p2 in zip(phoneBook, phoneBook[1:]):
            if p2.startswith(p1):
                return False
        return True
'''