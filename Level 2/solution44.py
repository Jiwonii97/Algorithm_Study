# 코딩테스트 연습 / 2020 카카오 인턴십 / 수식 최대화
# permutations를 통해 규칙을 정하고 그때마다 최선의 값을 찾는 방식(그리드 알고리즘 문제)

from itertools import permutations as pt
def calc(num1, point, num2):
    if point == "+":
        return str(int(num1)+int(num2))
    elif point == "-":
        return str(int(num1)-int(num2))
    else:
        return str(int(num1)*int(num2))

def solution(expression):
    result = []
    calculate = ["+", "-", "*"]
    order_case = pt(calculate,3)
    
    split_expression = []
    num = ""
    for e in expression:
        num+=e
        if num.isdigit():
            continue
        else:
            split_expression.append(num[:-1])
            split_expression.append(num[-1])
            num = ""
        
    split_expression.append(num)
    
    # 각 경우의 수를 확인해 계산하는 문제
    for order in order_case:
        tmp = split_expression.copy()
        for o in order:
            while o in tmp:
                idx = tmp.index(o)
                num = calc(tmp[idx-1],tmp[idx],tmp[idx+1])
                tmp = tmp[:idx-1]+[num]+tmp[idx+2:]
              
        temp = int(tmp[-1]) if int(tmp[-1]) >= 0 else -int(tmp[-1])
        result.append(temp)

    return max(result)

print(solution("100-200*300-500+20"))           # 60420
print(solution("50*6-3*2"))                 # 300

'''
    < 다른 풀이 >
    1. 
    import re
    from itertools import permutations

    def solution(expression):
        #1
        op = [x for x in ['*','+','-'] if x in expression]
        op = [list(y) for y in permutations(op)]
        ex = re.split(r'(\D)',expression)

        #2
        a = []
        for x in op:
            _ex = ex[:]
            for y in x:
                while y in _ex:
                    tmp = _ex.index(y)
                    _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                    _ex = _ex[:tmp]+_ex[tmp+2:]
            a.append(_ex[-1])

        #3
        return max(abs(int(x)) for x in a)
        
        2.
        def solution(expression):
            operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
        answer = []
        for op in operations:
            a = op[0]
            b = op[1]
            temp_list = []
            for e in expression.split(a):
                temp = [f"({i})" for i in e.split(b)]
                temp_list.append(f'({b.join(temp)})')
            answer.append(abs(eval(a.join(temp_list))))
        return max(answer)
'''