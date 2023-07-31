# https://school.programmers.co.kr/learn/courses/30/lessons/181888

def solution(num_list, n):
    answer = []
    cnt = 0

    for index, num in enumerate(num_list):
        if cnt == 0:
            answer.append(num)
            cnt = n-1
        else:
            cnt -= 1

    return answer
