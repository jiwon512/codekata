'''
문제: 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 
      단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12935
날짜: 2025-06-27
'''

# 첫번째 생각
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))                            # At firt, I coded it as 'return arr.remove(min(arr))', but it returned NONE
        return arr                                      # why? cuz arr.remove(min(arr)) only removes the value from the list—it doesn’t return the modified list.



# more Pythonic
def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))                                # readability, clarity, maintainability > way better
    return arr
