'''
문제: String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요.
     seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12919
날짜: 2025-06-10
'''

def solution(seoul):
    kim_idx = seoul.index('Kim')          # 특정한 값의 인덱스 찾기
    return f"김서방은 {kim_idx}에 있다"       # fstring 사용
