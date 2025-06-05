'''
문제 : 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12932
날짜 : 2025-06-05
'''

def solution(n):
    return [int(i) for i in str(n)[::-1]]


# list(), map() 사용

def solution(n):
    return list(map(int, reversed(str(n))))      # list(iterable)        : 반복 가능한 데이터를 입력받아 리스트로 만들어 리턴
                                                 # map(f, iterable)      : 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴
                                                 # reversed()            : 문자열 뒤집기
                                                 # str()                 : 문자열 형태로 객체 변환
