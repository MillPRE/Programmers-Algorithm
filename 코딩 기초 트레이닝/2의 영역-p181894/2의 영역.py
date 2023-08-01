# https://school.programmers.co.kr/learn/courses/30/lessons/181894

def solution(arr):
    answer = []
    flag = False

    if arr.count(2) == 0:
        return [-1]
    elif arr.count(2) == 1:
        return [2]
    else:
        first = arr.index(2)
        arr.reverse()
        last = arr.index(2)
        arr.reverse()
        answer = arr[first:-last]

    return arr if len(answer) == 0 else answer
