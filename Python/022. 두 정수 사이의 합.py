'''
문제 : 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
      예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12912
날짜 : 2025-06-09
'''

# 내가 작성한 답안

def solution(a, b):
    answer = 0
    if a <= b:
        for i in range(a, b+1):
            answer += i
    else:  
        for i in range(b, a+1):
            answer += i

    return answer                    # 코드가 너무 길다...



# 1. 다른 방법

def solution(a, b):
    answer = 0 
    for i in range(min(a, b), max(a, b)+1):
        answer += i
    return answer


# 2. 다른 방법

def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))
