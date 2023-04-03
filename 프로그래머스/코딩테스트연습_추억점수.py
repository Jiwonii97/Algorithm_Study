#  코딩테스트 연습 / 연습문제 / 추억 점수

def solution(name, yearning, photo):
    answer = []

    memory = {k: v for k, v in zip(name, yearning)}
    for p in photo:
        answer.append(sum([memory[i] for i in p if i in memory]))

    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [
      ["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"], [11, 1, 55], [
      ["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
      [["may"], ["kein", "deny", "may"], ["kon", "coni"]]))
