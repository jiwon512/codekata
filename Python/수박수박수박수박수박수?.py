'''
문제: 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
     예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12922
날짜: 2025-06-30
'''


def solution(n):
    return ('수박' * (n//2)) + ('수' if n%2 else '')

# 파이썬에서 if 뒤에 값이 0또는 NaN이 나오면 False, 값이 있다면 True
