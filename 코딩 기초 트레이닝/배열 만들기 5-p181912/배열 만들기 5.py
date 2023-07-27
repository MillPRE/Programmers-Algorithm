# https://school.programmers.co.kr/learn/courses/30/lessons/181912

def solution(intStrs, k, s, l):
    answer = []

    for i in intStrs:
        i = i[s:s+l]
        if(int(i) > k):
            answer.append(int(i))

    return answer
