# Algorithm_Study

- Level 1  
solution2. 신고 결과 받기 (코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT) : list comprehension, set, index 활용
solution3. 로또의 최고 순위와 최저 순위 (코딩테스트 연습 / 2021 Dev-Matching: 웹 백엔드 개발자(상반기)) : 경우의 수를 따지는 단순 수학 문제
solution4. 신규 아이디 추천 (*****) ( 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT ) : 정규식 활용 문제 
solution5. 숫자 문자열과 영단어 ( 코딩테스트 연습 / 2021 카카오 채용연계형 인턴십 ) : 딕셔너리를 활용힌 문자열 replace 문제
solution6. 키패드 누르기 ( 코딩테스트 연습 / 2020 카카오 인턴십 ) : 단순 구현 문제
solution7. 크레인 인형뽑기 게임 ( 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 ) : list slicing 대신 pop를 사용하여 원하는 인덱스의 원소 제거
solution8. 없는 숫자 더하기 ( 코딩테스트 연습 / 월간 코드 챌린지 시즌3 ) : 단순 수학 연산, sum() 활용
solution9. 음양 더하기 ( 코딩테스트 연습 / 월간 코드 챌린지 시즌2 ) : zip과 list comprehension, sum 사용
solution10. 내적 ( 코딩테스트 연습 / 월간 코드 챌린지 시즌1 ) : zip과 list comprehension, sum 사용
solution11. 소수 만들기 ( 코딩테스트 연습 / Summer/Winter Coding(~2018) ) : 모든 조합의 경우를 구해주는 함수 : from itertools import combinations -> list(combinations(nums, 3))
solution12. K번째수 ( 코딩테스트 연습 / 정렬 ) : map은 리스트의 요소를 지정된 타입 or 함수로 처리해주는 함수 -> list(map(형식, 대상)) : list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)), sorted(리스트) -> 정렬된 리스트를 리턴
solution13. 모의고사 ( 코딩테스트 연습 / 완전탐색 ) : enumerate로 인덱스와 해당 리스트 값을 한번에 가져올 수 있음, 나머지 연산을 통해 반복적인 요소 제한 (곱하는 거 보다 쉬운 방법)
solution14. 체육복 ( 코딩테스트 연습 / 탐욕법(Greedy) ) : 그리디 알고리즘 활용 예시
solution15. 폰켓몬 ( 코딩테스트 연습 / 찾아라 프로그래밍 마에스터 ) : 중복을 제거하는 가장 쉬운 방법 : list를 set으로 변경
solution16. 실패율 ( 코딩테스트 연습 / 2019 KAKAO BLIND RECRUITMENT ) : sorted -> dictionary를 넣으면 sort된 list를 반환해줌, result는 dictionary이므로 sorted에 result를 그냥 넘기면 result의 keys가 들어감, keys는 생략이 가능, lambda는 기준을 result[x]: 즉 value로 정렬되므로 key가 정렬값으로 사용
solution17. 완주하지 못한 선수 ( 코딩테스트 연습 / 해시 ) : collections.Counter을 통해 각 값이 몇개씩 들어있는지 한번에 확인 가능(리턴 : 딕셔너리), 딕셔너리끼리의 차는 각 키값의 데이터차로 구해짐
