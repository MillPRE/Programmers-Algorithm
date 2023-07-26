# https://school.programmers.co.kr/learn/courses/30/lessons/181831

def solution(arr):
    N = len(arr)

    for i in range(N):
        for j in range(N):
            if arr[i][j] != arr[j][i]:
                return 0

    return 1
