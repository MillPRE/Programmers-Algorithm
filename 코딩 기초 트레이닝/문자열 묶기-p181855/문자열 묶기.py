# https://school.programmers.co.kr/learn/courses/30/lessons/181855

def solution(strArr):
    dic = {}
    answer = []

    for s in strArr:
        if not len(s) in dic:
            dic[len(s)] = 1
        else:
            dic[len(s)] += 1

    for k in dic:
        answer.append(dic[k])

    return max(answer)
