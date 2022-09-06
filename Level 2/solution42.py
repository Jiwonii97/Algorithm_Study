# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 방문 길이
# 좌표의 크기는 [-5:5][-5:5]

def solution(dirs):
    save = []
    control = {"U":[0,1],"D":[0,-1],"L":[-1,0],"R":[1,0]}
    movement = list(dirs)
    
    point = [0,0]       # 시작 좌표(원점)
    for move in movement:
        next_point = [x+y for x,y in zip(point,control[move])]      # 다음으로 이동하는 좌표
        
        # 좌표를 넘어가는 경우
        if not(-5 <= next_point[0] <= 5) or not(-5 <= next_point[1] <= 5): continue
        
        # 한번 지나온 길이 아닌 경우
        if sorted([point,next_point]) not in save:
            save.append(sorted([point,next_point]))
            
        point = next_point      # 업데이트
    
    return len(save)

print(solution("ULURRDLLU"))        # 7
print(solution("LULLLLLLU"))        # 7