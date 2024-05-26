'''
[배열과 리스트] 실전문제

문제 분석
1. 파이썬 리스트 자료구조 이용  
2. 주어진 숫자를 리스트 형태로 저장  
3. 해당 리스트를 index를 이용하여 탐색  
4. 각 자릿수의 값을 정수형으로 변환하여 더하기

슈도코드
n값 받기  
numbers 변수에 list 함수를 이용하여 숫자를 한 자리씩 나누어 받기  
sum 변수 선언  

for numbers 탐색:  
    sum 변수에 numbers에 있는 각 자릿수를 가져와 더하기  
'''

n = input()
numbers = list(input())

sum = 0

for i in numbers:
    sum = sum + int(i)

print(sum)