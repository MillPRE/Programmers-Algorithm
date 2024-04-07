import math


def solution(progresses, speeds):
    answer = []
    diff = []

    for idx in range(len(progresses)):
        diff.append(math.ceil((100 - progresses[idx]) / speeds[idx]))

    t = diff[0]
    cnt = 1
    for idx in range(1, len(diff)):
        if diff[idx] <= t:
            cnt += 1
        else:
            answer.append(cnt)
            t = diff[idx]
            cnt = 1

    answer.append(cnt)
    return answer