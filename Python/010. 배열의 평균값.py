'''
문제 : 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120817
날짜 : 2025-06-04
'''

def solution(numbers):
    return sum(numbers)/len(numbers)
  

# 다른 풀이, numpy 사용

import numpy as np            # numpy는 파이썬의 기본 기능이 아니기 때문에 import 해주지 않으면 Numpy의 함수들을 알 수 없다.

def solution(numbers):
    return np.mean(numbers)
