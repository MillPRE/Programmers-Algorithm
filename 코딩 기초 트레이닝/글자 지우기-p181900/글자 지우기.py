# https://school.programmers.co.kr/learn/courses/30/lessons/181900

def solution(my_string, indices):
    answer = ''
    my_string = list(my_string)

    for index, s in enumerate(my_string):
        if not index in indices:
            answer += s

    return answer
