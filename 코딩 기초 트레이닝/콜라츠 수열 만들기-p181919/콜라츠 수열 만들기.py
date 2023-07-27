# https://school.programmers.co.kr/learn/courses/30/lessons/181919

def solution(n):
    answer = [n]
    current = n

    while current > 1:
        if current % 2 == 0:
            current = current / 2
        else:
            current = current * 3 + 1
        answer.append(current)

    return answer
