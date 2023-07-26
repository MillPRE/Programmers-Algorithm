# https://school.programmers.co.kr/learn/courses/30/lessons/181926

def solution(n, control):
    answer = n

    dic = {
        'w': 1,
        's': -1,
        'd': 10,
        'a': -10,
    }

    control = list(control)

    for c in control:
        answer += dic[c]

    return answer
