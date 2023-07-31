# https://school.programmers.co.kr/learn/courses/30/lessons/181924

def solution(arr, queries):
    for q in queries:
        [i, j] = q
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    return arr
