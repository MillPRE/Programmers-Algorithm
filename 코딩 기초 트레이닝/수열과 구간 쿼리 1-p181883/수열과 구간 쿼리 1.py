# https://school.programmers.co.kr/learn/courses/30/lessons/181883

def solution(arr, queries):
    answer = arr

    for index, query in enumerate(queries):
        for i, a in enumerate(arr):
            if i >= query[0] and i <= query[1]:
                answer[i] += 1

    return answer
