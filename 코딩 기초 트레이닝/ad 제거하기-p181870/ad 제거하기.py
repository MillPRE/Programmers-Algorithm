# https://school.programmers.co.kr/learn/courses/30/lessons/181870

def solution(strArr):
    answer = []

    for s in strArr:
        if 'ad' not in s:
            answer.append(s)

    return answer
