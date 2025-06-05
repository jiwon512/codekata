'''
문제 : 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12928
날짜 : 2025-06-05
'''

def solution(n):
  
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
          answer += i

    return answer


# 컴프리헨션 사용

def solution(n):
  return sum(i for i in range(1, n+1) if n % i == 0)
