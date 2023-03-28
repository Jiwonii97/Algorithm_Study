# 코딩테스트 연습 / 연습문제 / 카드 뭉치

def solution(cards1, cards2, goal):
    answer = ''

    card1, card2 = cards1.pop(0), cards2.pop(0)
    for tgt_word in goal:
        if tgt_word == card1:
            if cards1:
                card1 = cards1.pop(0)
            else:
                card1 = ""
        elif tgt_word == card2:
            if cards2:
                card2 = cards2.pop(0)
            else:
                card2 = ""
        else:
            return "No"
    else:
        return "Yes"


print(solution(["i", "drink", "water"], ["want", "to"],
      ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"],
      ["i", "want", "to", "drink", "water"]))
