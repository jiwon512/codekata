'''
문제 : 숫자 비교하기
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120807
날짜 : 2025-06-02
'''

def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer
  
# 먼저 작성된 양식에 return answer이 있어서 answer 변수로 설정한 뒤  진행하였지만 아래와 같이 바로 return 가능

def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1

# 또 다른 풀이

def solution(num1, num2):
    return 1 if num1 == num2 else -1
