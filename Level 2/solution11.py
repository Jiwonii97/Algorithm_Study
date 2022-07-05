def solution(phone_book):
    pb = sorted(phone_book, key = lambda x: (len(x), x))
    
    for i, phone in enumerate(pb):
        size_ = len(phone)
        for j, check in enumerate(pb):
            if i!=j and phone == check[:size_]:
                return False
    
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
print(solution(["13","123","1235","567","88"]))