# https://school.programmers.co.kr/learn/courses/30/lessons/181830

def solution(arr):
    if len(arr) > len(arr[0]):
        LEN = len(arr) - len(arr[0])
        for a in arr:
            a += [0 for i in range(LEN)]
        # 열의 수가 행의 수보다 많은 경우
    elif len(arr) < len(arr[0]):
        # 행의 수가 열의 수보다 많은 경우
        for i in range(len(arr[0]) - len(arr)):
            arr.append([0 for i in range(len(arr[0]))])

    return arr
