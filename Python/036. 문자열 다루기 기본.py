'''
문제: 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12918
날짜: 2025-07-08
'''

def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()

# isdigit() : 문자열 안에 숫자만 있는지 판별하는 메서드
