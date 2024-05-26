'''
[구간합] 실전문제 1

문제분석
1. 배열이 무한히 확장되는 경우를 고려하여 설계
2. 합배열을 만들고, 배열 자체를 계산하는 방법

슈도코드

n(리스트 크기), m(질의 수), A(원본 리스트), D(합 배열)

for n만큼 반복:
    원본 리스트 데이터 저장

for i부터 n까지 반복:
    for j를 1부터 n까지 반복:
        합 배열 저장
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for m만큼 반복:
    질의에 대한 결과 계산 및 출력
        결과 = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
'''

import sys
input = sys.stdin.readline
'''
input = sys.stdin.readline
- Python에서 입력을 받는 속도를 향상시켜주는 역할

기본적으로 Python의 input() 함수는 사용자의 입력을 받으면서, 
공백문자(예: 줄바꿈)를 제거하는 등의 추가적인 작업을 수행하기 때문에 상대적으로 느릴 수 있습니다.
반면 sys.stdin.readline은 줄바꿈 문자를 포함한 한 줄의 문자열을 빠르게 입력받기 때문에, 
많은 양의 데이터를 빠르게 입력받아야 하는 경우 (예: 알고리즘 문제에서의 대량의 데이터 입력)에 훨씬 효율적입니다.

다만, sys.stdin.readline을 사용할 때에는 문자열의 마지막에 줄바꿈 문자가 포함되기 때문에, 
이를 제거하기 위해 종종 strip()을 사용해야 할 수 있습니다.

따라서 알고리즘 문제를 풀 때 입출력의 양이 많고 빠른 입출력이 요구되는 경우, 
input() 대신 sys.stdin.readline을 사용하여 시간 초과를 방지할 수 있습니다.
'''

n, m = map(int, input().split())
A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1,n+1):
    for j in range(1,n+1):
        #구간 합 구하기
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 구간 합 배열로 질의에 답변
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1 -1]
    print(result)

