# https://school.programmers.co.kr/learn/courses/30/lessons/181905

def solution(my_string, s, e):
    answer = my_string[0:s]
    tmp = my_string[s:e+1]
    tmp = tmp[::-1]
    answer += tmp
    answer += my_string[e+1:]

    return answer
