# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    dic = {}
    answer = []
    for idx in range(len(s)):
        keys = dic.keys()
        if s[idx] not in keys:
            dic[s[idx]] = idx
            answer.append(-1)
        else:
            answer.append(idx - dic[s[idx]])
            dic[s[idx]] = idx
    return answer