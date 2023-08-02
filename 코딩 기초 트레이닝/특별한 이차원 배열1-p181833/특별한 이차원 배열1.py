# https://school.programmers.co.kr/learn/courses/30/lessons/181833

def solution(n):
    answer = [[0 for j in range(n)] for i in range(n)]

    for index, i in enumerate(answer):
        answer[index][index] = 1

    return answer
