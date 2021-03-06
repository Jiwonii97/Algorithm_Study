# Algorithm_Study

## Level 2  
**solution1. 최댓값과 최솟값 ( 연습문제 )** : 단순 수학 문제  
**solution2. 최솟값 만들기 ( 연습문제 )** :zip 활용 문제  
**solution3. 피보나치 수 ( 연습문제 )** : 단순 피보나치 문제  
**solution4. 행렬의 곱셈 ( 연습문제 )** : Asterisk(*)을 언패킹 컨테이너로 사용 - 이차원 리스트로 선언된 B를 언패킹하여 1차원으로 만들고 zip하여 열로 나타냄  
**solution20.  124 나라의 숫자 ( 연습문제 )** : 3진법 변환 문제와 유사, divmod 활용 예시  
**solution21. 오픈채팅방 ( 2019 KAKAO BLIND RECRUITMENT )** : 딕셔너리를 활용한 해시 문제  
**solution32. 짝지어 제거하기 ( 2017 팁스타운 )** : Stack 활용 문제  
**solution33. 멀쩡한 사각형 ( Summer/Winter Coding(2019) )** : 최대 공약수를 찾아 효율적으로 검색  
**solution34. 행렬 테두리 회전하기 ( 2021 Dev-Matching: 웹 백엔드 개발자(상반기) )** : 큐를 이용해 노가다로 품, 근데 다 비슷한게 푼듯  
**solution35. 문자열 압축 ( 2020 KAKAO BLIND RECRUITMENT )** : 완전탐색 문제, 일정 문자열 길이를 반복해나가며 최솟값을 찾아나가는 구현 문제  
  
### - 스택 / 큐  
**solution5. 프린터 ( 스택/큐 )** : queue와 deque 활용  
**solution6. 다리를 지나는 트럭 ( 스택/큐 )** : collection, deque 사용, 시간을 따로 계산하지 않고 popleft()와 직접 0과 함께 숫자를 넣어 시간 계산 진행  
**solution7. 다리를 지나는 트럭 ( 스택/큐 )** : collection, deque 사용, 시간을 따로 계산하지 않고 popleft()와 직접 0과 함께 숫자를 넣어 시간 계산 진행, reverse를 통한 -1 인덱스 사용  
**solution8. 주식가격 ( 스택/큐 )** : Stack 활용  
**solution22. 올바른 괄호 ( 스택/큐 )** : 일반적인 스택 활용, try-except를 사용한 stack 처리   
  
### - 정렬  
**solution9. H-Index ( 정렬 )** : 오름차순으로 정렬후 조건에 맞게 문제 풀이  
**solution10. 가장 큰 수 ( 정렬 )** : 문자열을 반복시켜 문자값의 크기를 비교해 정렬  
  
### - 해시  
**solution11. 전화번호 목록 ( 해시 )** : startswith를 사용해 굳이 문자열 길이를 따로 구하지 않고도 해당 단어로 시작하는지 확인 가능  
**solution12. 위장 ( 해시 )** : (a+1)(b+1)(c+1)-1 수식을 활용한 경우의 수 계산, Counter, reduce를 활용해 딕셔너리 계산  
**solution13. 베스트앨범 ( 해시 )** : 카테고리 별로 딕셔너리 항목을 나누고 정렬을 통해 높은 순서로 데이터를 가져옴 
  
### - 힙(Heap)   
**solution14. 더 맵게 ( 힙(Heap) )** : heapq 라이브러리를 활용한 우선순위 큐 계산  
**solution15. 디스크 컨트롤러(LV3) ( 힙(Heap) )** : os 컨트롤러인 SJF를 물어보는 문제, 우선순위 큐를 활용한 연산 진행  
**solution16. 이중우선순위큐(LV3) ( 힙(Heap) )** : heapq 라이브러리를 활용한 우선순위 큐 계산  
  
### - 완전탐색  
**solution17. 소수 찾기 ( 완전탐색 )** : permutations로 순열을 구하고 완전탐색을 통해 경우의 수를 찾음  
**solution18. 카펫 ( 완전탐색 )** : 넓이를 이용한 완전탐색 진행  
**solution23. 피로도 ( 완전탐색 )** : 순열을 통해 모든 경우의 수를 구하고 전체의 경우의 수를 탐색  
**solution24. 전력망을 둘로 나누기 ( 완전탐색 )** : deque 형태로 사이클을 돌리며 모든 전력망을 두 그룹으로 나눌때까지 반복문을 진행  
**solution25. 모음사전 ( 완전탐색 )** : 중복순열을 통해 전체 리스트를 만들고 정렬 후 직접 탐색, 등비수열의 합 활용 가능(블로그 참고)  
  
### - 그리디(탐욕법)  
**solution26. 큰 수 만들기 ( 탐욕법(Greedy) )** : 스택을 활용한 그리디 문제  
**solution27. 구명보트 ( 탐욕법(Greedy) )** : 더블 포인터를 사용한 그리디 문제  
**solution28. 섬 연결하기(LV3) ( 탐욕법(Greedy) )** : 크루스칼 알고리즘 활용 : 정렬 후, 가치가 낮은 간선부터 선택하여 각 지점을 연결 ( 그리디 )  
**solution29. 조이스틱 ( 탐욕법(Greedy) )** : 그리디 알고리즘 활용하여 코드 진행하며 최소값을 계속 갱신하는 문제   
**solution30. 단속카메라(LV3) ( 탐욕법(Greedy) )** : 이전 solution29 응용, 인덱스를 넘어가면서 이전꺼와 비교하며 조건에 맞는 값을 도출  

### - 깊이/너비 우선 탐색(DFS/BFS)  
**solution19. 타겟 넘버 ( 깊이/너비 우선 탐색(DFS/BFS) )** : 전역변수와 재귀를 활용한 DFS 문제  
**solution31. 게임 맵 최단거리 ( 깊이/너비 우선 탐색(DFS/BFS) )** : deque를 이용해 하나씩 좌표를 뽑아서 해당 부분을 확인해 나가는 방식의 BFS 문제, 좌표를 따질때 가로/세로 크기를 확실하게 확인  