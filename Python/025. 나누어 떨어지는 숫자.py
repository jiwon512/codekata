'''
문제: array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
     divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12910
날짜: 2025-06-10
'''

def solution(arr, divisor):
    answer = [arr[i] for i in range(len(arr)) if arr[i] % divisor == 0] 
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)


# simplifed version

def solution(arr,divisor):
    answer = [num for num in arr if num % divisor == 0]
    return sorted(answer) if answer else [-1]               # if answer: checks if the list is not empty
                                                            # in Python, empty lists are False in a boolean context
