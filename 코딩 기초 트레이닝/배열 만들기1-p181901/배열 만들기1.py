# https://school.programmers.co.kr/learn/courses/30/lessons/181901

def solution(n, k):
    answer = [k]

    while answer[len(answer) -1] < n:
        answer.append(answer[len(answer) -1] + k)

    return answer[:-1] if answer[len(answer) -1] > n else answer
