'''
링크: https://school.programmers.co.kr/learn/courses/30/lessons/77884
문제: 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
날짜: 2025-07-02
'''

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count +=1
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer 



# 변수 선언 위치가 굉장히 헷갈림 이런 문제로 많이 연습해야겠다...
