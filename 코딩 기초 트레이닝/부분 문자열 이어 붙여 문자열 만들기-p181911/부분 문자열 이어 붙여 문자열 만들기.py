# https://school.programmers.co.kr/learn/courses/30/lessons/181911

def solution(my_strings, parts):
    answer = ''

    for index, p in enumerate(parts):
        answer += my_strings[index][p[0]:p[1]+1]

    return answer
