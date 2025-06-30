'''
문제: 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
     이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/70128
날짜: 2025-06-30
'''

# 내가 푼 풀이

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

  
# 다른 사람 풀이

def solution(a,b):
    return sum(x*y for x, y in zip(a,b))

# zip() 함수는 여러 개의 리스트(또는 반복 가능한 자료형)를 짝지어서 각 리스트의 같은 위치에 있는 요소들을 튜플로 묶어주는 함수
