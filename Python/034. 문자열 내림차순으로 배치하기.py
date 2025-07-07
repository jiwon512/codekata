'''
문제: 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
     s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12917
날짜: 2025-07-07
'''

def solution(s):
    char = sorted(s, reverse=True) 
    return ''.join(char)  # join 앞에는 '' or ',' , '-' 같은 구분자가 무조건 들어가줘야함.

# sorted() vs sort()
# sorted() : 함수, 만약 변수가 문자열이나 숫자열이더라도 정렬하여 리스트의 형태로 반환함. 이 때 정렬된 값이 저장되지는 않음.
# sort() : 매서드, 리스트 형태의 변수를 정렬해줌. 이때 값 자체가 변수에 새롭게 저장되며, sort()의 반환값은 NONE


# 만약 sort() 사용하는 경우
def soluion(s):
    char = list(s)          # 먼저 리스트로 변환해줌.
    char.sort(reverse=True)
    return ''.join(char)
