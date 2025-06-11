'''
문제: 어떤 정수들이 있습니다. 
     이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
     실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
링크: https://school.programmers.co.kr/learn/courses/30/lessons/76501
날짜: 2025-06-11
'''

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:                              # The list 'signs' is the boolean.
            answer += absolutes[i]                # writing if signs[i]:
        else:                                     # If signs[i] is True, the condition will be true, and the code inside will run
            answer -= absolutes[i]
    return answer



# 다른 사람 풀이

def solution(absolutes, signs):
  answer = sum(absolutes if signs else -absolutes for absolutes, signs in zip(absolutes, signs))

# The zip() function pairs up elements from two (or more) lists
