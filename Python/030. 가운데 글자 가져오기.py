'''
문제: 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12903
날짜: 2025-06-27
'''

# 내 풀이
def solution(s):
    if len(s) % 2 == 0:
        mid_num = len(s)//2
        return s[mid_num-1:mid_num+1]
    else:
        mid_num = len(s)//2
        return s[mid_num]


# 다른사람 풀이
def solution(s):
    return s[(len(s)-1)//2 : len(s)//2 + 1]

