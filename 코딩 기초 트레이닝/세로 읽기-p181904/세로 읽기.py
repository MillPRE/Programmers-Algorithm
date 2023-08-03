# https://school.programmers.co.kr/learn/courses/30/lessons/181904

def solution(my_string, m, c):
    answer = ''
    my_string = list(my_string)
    cnt = 0

    for idx, v in enumerate(my_string):
        cnt += 1
        if cnt == c:
            answer += v

        if cnt == m:
            cnt = 0

    return answer
