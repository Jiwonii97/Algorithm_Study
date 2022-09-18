# Algorithm_Study

## Level 1  
**solution1. 약수의 합 ( 코딩테스트 연습 / 연습문제 )** : 나누어지는 약수만 찾아 sum으로 더함  
**solution2. 신고 결과 받기 (코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT)** : list comprehension, set, index 활용  
**solution3. 로또의 최고 순위와 최저 순위 (코딩테스트 연습 / 2021 Dev-Matching: 웹 백엔드 개발자(상반기))** : 경우의 수를 따지는 단순 수학 문제  
**solution4. 신규 아이디 추천 (😝😝😝😝😝) ( 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT )** : 정규식 활용 문제   
**solution5. 숫자 문자열과 영단어 ( 코딩테스트 연습 / 2021 카카오 채용연계형 인턴십 )** : 딕셔너리를 활용힌 문자열 replace 문제  
**solution6. 키패드 누르기 ( 코딩테스트 연습 / 2020 카카오 인턴십 )** : 단순 구현 문제  
**solution7. 크레인 인형뽑기 게임 ( 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 )** : list slicing 대신 pop를 사용하여 원하는 인덱스의 원소 제거  
**solution8. 없는 숫자 더하기 ( 코딩테스트 연습 / 월간 코드 챌린지 시즌3 )** : 단순 수학 연산, sum() 활용  
**solution9. 음양 더하기 ( 코딩테스트 연습 / 월간 코드 챌린지 시즌2 )** : zip과 list comprehension, sum 사용  
**solution10. 내적 ( 코딩테스트 연습 / 월간 코드 챌린지 시즌1 )** : zip과 list comprehension, sum 사용  
**solution11. 소수 만들기 ( 코딩테스트 연습 / Summer/Winter Coding(~2018) )** : 모든 조합의 경우를 구해주는 함수 : from itertools import combinations -> list(combinations(nums, 3))  
**solution12. K번째수 ( 코딩테스트 연습 / 정렬 )** : map은 리스트의 요소를 지정된 타입 or 함수로 처리해주는 함수 -> list(map(형식, 대상)) : list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)), sorted(리스트) -> 정렬된 리스트를 리턴  
**solution13. 모의고사 ( 코딩테스트 연습 / 완전탐색 )** : enumerate로 인덱스와 해당 리스트 값을 한번에 가져올 수 있음, 나머지 연산을 통해 반복적인 요소 제한 (곱하는 거 보다 쉬운 방법)
**solution14. 체육복 ( 코딩테스트 연습 / 탐욕법(Greedy) )** : 그리디 알고리즘 활용 예시  
**solution15. 폰켓몬 ( 코딩테스트 연습 / 찾아라 프로그래밍 마에스터 )** : 중복을 제거하는 가장 쉬운 방법 : list를 set으로 변경  
**solution16. 실패율 ( 코딩테스트 연습 / 2019 KAKAO BLIND RECRUITMENT )** : sorted -> dictionary를 넣으면 sort된 list를 반환해줌, result는 dictionary이므로 sorted에 result를 그냥 넘기면 result의 keys가 들어감, keys는 생략이 가능, lambda는 기준을 result[x]: 즉 value로 정렬되므로 key가 정렬값으로 사용  
**solution17. 완주하지 못한 선수 ( 코딩테스트 연습 / 해시 )** : collections.Counter을 통해 각 값이 몇개씩 들어있는지 한번에 확인 가능(리턴 : 딕셔너리), 딕셔너리끼리의 차는 각 키값의 데이터차로 구해짐  
**solution18. 약수의 개수와 덧셈 ( 코딩테스트 연습 / 월간 코드 챌린지 시즌2 )** : 제곱수인 경우 약수의 개수가 홀수 인것을 활용한 제곱수를 이용한 방식  
**solution19. 3진법 뒤집기 ( 코딩테스트 연습 / 월간 코드 챌린지 시즌1 )** : 정수의 진수 변환을 보여주는 좋은 예  
**solution20. 예산 ( 코딩테스트 연습 / Summer/Winter Coding(~2018) )** : 유사 knapsack 문제 _ 정렬후 낮은 값을 빼어 많은 양이 남도록 함  
**solution21. 두 개 뽑아서 더하기 ( 코딩테스트 연습 / 월간 코드 챌린지 시즌1 )** : sorted 하는거 놓치지 않아야 할듯 (정석풀이) _ 출력값에 따라 정렬유무 판단  
**solution22. 2016년 ( 코딩테스트 연습 / 연습문제 )** : 단순 수학 구현 문제  
**solution23. 최소직사각형 ( 코딩테스트 연습 / 위클리 챌린지 )** : min, max를 활용한 수학 구현 문제  
**solution24. 나머지가 1이 되는 수 찾기 ( 코딩테스트 연습 / 월간 코드 챌린지 시즌3 )** : 나머지가 1인 수를 찾으면 되므로 1을 뺐을때 나눠지는 수를 찾으면 됨  
**solution25. 부족한 금액 계산하기 ( 코딩테스트 연습 / 월간 코드 챌린지 시즌1 )** : max, sum을 활용한 수학 구현문제  
**solution26. [1차] 비밀지도 ( 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT )** : bin으로 수를 이진법으로 바꾸고 rjust로 특정한 문자열 길이를 맞춤, replace로 문자열 교체  
**solution27. 가운데 글자 가져오기 ( 코코딩테스트 연습 / 연습문제 )** : slicing 사용  
**solution28. [1차] 다트 게임 (😝😝😝😝😝) ( 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT )** : 정규식 활용 문제  
**solution29. 같은 숫자는 싫어 ( 코딩테스트 연습 / 연습문제 )** : 연속된 숫자가 나오지 않게 처리, 원소를 직접 리스트에 넣어 비교  
**solution30. 나누어 떨어지는 숫자 배열 ( 코딩테스트 연습 / 연습문제 )** : or을 사용하여 리스트에 아무것도 없으면 [-1]이 포함  
**solution31. 두 정수 사이의 합 ( 코딩테스트 연습 / 연습문제 )** : range, sum 활용  
**solution32. 문자열 내 마음대로 정렬하기 ( 코딩테스트 연습 / 연습문제 )** : key값으로 lambda 함수를 활용해 원하는 방식으로 정렬시킴  
**solution33. 문자열 내 p와 y의 개수 ( 코딩테스트 연습 / 연습문제 )** : upper, lower 활용한 비교  
**solution34. 문자열 내림차순으로 배치하기 ( 코딩테스트 연습 / 연습문제 )** : join 활용 방법  
**solution35. 문자열 다루기 기본 ( 코딩테스트 연습 / 연습문제 )** : isdigit() 활용  
**solution36. 서울에서 김서방 찾기 ( 코딩테스트 연습 / 연습문제 )** : index로 원하는 원소 인덱스 찾기  
**solution37. 소수 찾기 ( 코딩테스트 연습 / 연습문제 )** : 에라토스테네스의 체  
**solution38. 수박수박수박수박수박수? ( 코딩테스트 연습 / 연습문제 )** : 문자열 slicing  
**solution39. 문자열을 정수로 바꾸기 ( 코딩테스트 연습 / 연습문제 )** : 문자열에 -가 있어도 정수로 변환시켜줌  
**solution40. 시저 암호 ( 코딩테스트 연습 / 연습문제 )** : 나머지 연산 활용, hr : char형 타입, ord : 아스키코드 번호  
**solution41. 이상한 문자 만들기 ( 코딩테스트 연습 / 연습문제 )** : upper, lower 활용  
**solution42. 자릿수 더하기 ( 코딩테스트 연습 / 연습문제 )** : sum 활용  
**solution43. 자연수 뒤집어 배열로 만들기 ( 코딩테스트 연습 / 연습문제 )** : map으로 문자열을 숫자로 변환, reversed로 문자열 뒤집기 활용  
**solution44. 정수 내림차순으로 배치하기 ( 코딩테스트 연습 / 연습문제 )** : 정렬 후 reverse 시켜 이어붙임  
**solution45. 정수 제곱근 판별 ( 코딩테스트 연습 / 연습문제 )** : sqrt : 제곱근, pow : 제곱수  
**solution46. 제일 작은 수 제거하기 ( 코딩테스트 연습 / 연습문제 )** : lambda 함수 활용  
**solution47. 짝수와 홀수 ( 코딩테스트 연습 / 연습문제 )** : 단순 구현 문제  
**solution48. 최대공약수와 최소공배수 ( 코딩테스트 연습 / 연습문제 )** : 최대공약수와 최소공배수  
**solution49. 콜라츠 추측 ( 코딩테스트 연습 / 연습문제 )** : 단순 수학 문제  
**solution50. 평균 구하기 ( 코딩테스트 연습 / 연습문제 )** : 단순 수학 문제  
**solution51. 하샤드 수 ( 코딩테스트 연습 / 연습문제 )** : sum 활용  
**solution52. 핸드폰 번호 가리기 ( 코딩테스트 연습 / 연습문제 )** : 단순 문자열 문제  
**solution53. 행렬의 덧셈 ( 코딩테스트 연습 / 연습문제 )** : zip과 리스트를 활용한 문제  
**solution54. x만큼 간격이 있는 n개의 숫자 ( 코딩테스트 연습 / 연습문제 )** : list comprehension  
**solution55. 직사각형 별찍기 ( 코딩테스트 연습 / 연습문제 )** : 단순 문자열 문제  