# https://school.programmers.co.kr/learn/courses/30/lessons/181922

def solution(arr, queries):
    answer = []

    for q in queries:
        s = q[0]
        e = q[1]
        k = q[2]

        for index, a in enumerate(arr):
            if index >= s and index <= e and index % k == 0:
                arr[index] += 1

    return arr
