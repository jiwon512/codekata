'''
문제 : 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
      다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12954
날짜 : 2025-06-05
'''

# First try

def solution(x, n):
    answer = []
    for i in range(1,n+1):
        y = x * i              # y라는 변수를 굳이 추가...
        answer.append(y)
    return answer


# 다른 사람 답변

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)
    return answer
