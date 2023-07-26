# https://school.programmers.co.kr/learn/courses/30/lessons/181868

def solution(my_string):
    answer = []
    my_string = my_string.split(" ")
    for m in my_string:
        if len(m.strip()) != 0:
            answer.append(m.strip())

    return answer
