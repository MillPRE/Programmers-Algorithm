# https://school.programmers.co.kr/learn/courses/30/lessons/181923

def solution(arr, queries):
    answer = []

    for index, q in enumerate(queries):
        s = q[0]
        e = q[1]
        k = q[2]

        tmp = arr[s:e+1]
        tmp = list(filter(lambda x: x > k, tmp))
        tmp.sort()

        if len(tmp) == 0:
            answer.append(-1)
        else:
            answer.append(tmp[0])

    return answer
