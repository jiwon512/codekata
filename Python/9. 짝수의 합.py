'''
문제 : 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120831
날짜 : 2025-06-04
'''

def solution(n):
    answer = 0                 # 결과값을 저장할 변수 초기화  
    for i in range(1, n+1):    # 파이썬 범위 지정 시에 주의 > n+1 전, n까지만 구함
        if i % 2 == 0:
            answer += i
    return answer

# 다른 풀이

def solution(n):
    return sum(i for i in range(1, n+1) if i%2 == 0) #제너레이터 표현식 사용

# 다른 풀이

def solution(n):
    return sum(i for i in range(2, n+1, 2))
