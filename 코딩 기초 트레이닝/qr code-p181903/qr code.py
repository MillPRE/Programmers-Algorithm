# https://school.programmers.co.kr/learn/courses/30/lessons/181903

def solution(q, r, code):
    answer = ''

    code = list(code)

    for index, c in enumerate(code):
        if(index % q == r):
            answer += c

    return answer
