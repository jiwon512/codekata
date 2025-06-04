'''
문제 : 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12931
날짜 : 2025-06-04
'''

# 제너레이터 컴프리헨션 사용식

def solution(n):
  return sum(int(i) for i in str(n))         # str : string의 약자로 숫자, 리스트, 기타 객체를 문자열(string)로 바꿔주는 함수
                                             # int : n의 자릿수들을 문자열로 변환하였으니 다시 숫자열로 변환.

                                           
# for문 사용

def solution(n):
  
  answer = 0
  for i in str(n):
    answer += int(i)

  return answer
