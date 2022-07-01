# 코딩테스트 연습 / 연습문제 / 직사각형 별찍기

a, b = map(int, input().strip().split(' '))

for n1 in range(b):
    for n2 in range(a):
        print('*',end="")
    print()
    
'''
    < 다른 풀이 >
    answer = ('*'*a +'\n')*b
    print(answer)
'''