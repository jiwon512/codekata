'''
문제 : 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
      n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12934#
날짜 : 2025-06-09
'''

def solution(n):
    x = int(n**0.5)         # 제곱근 구할 경우, 분수나 소수 제곱형태로 표현가능
    if x**2 == n
        return(x+1)**2
    else:
        return -1
