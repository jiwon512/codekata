'''
문제 : 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 solution 함수를 완성해주세요.
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120806
날짜 : 2025-06-02
'''

def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer

# 정수 부분을 리턴하는 것이므로 먼저 num1에 1000을 곱해준 뒤  몫 구하는 연산으로 구해줄 수 있음.

def solution(num1, num2):
    return num1 * 1000 // num2
