# https://school.programmers.co.kr/learn/courses/30/lessons/181931

def solution(a, d, included):
    current = 0
    answer = 0

    for index, value in enumerate(included):
        if index == 0:
            current += a
        else:
            current += d

        answer += current if value else 0


    return answer
