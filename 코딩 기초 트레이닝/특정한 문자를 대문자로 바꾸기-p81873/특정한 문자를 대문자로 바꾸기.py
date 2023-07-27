# https://school.programmers.co.kr/learn/courses/30/lessons/181873

def solution(my_string, alp):
    answer = ''

    for s in my_string:
        if(s == alp):
            answer += s.upper()
        else:
            answer += s

    return answer
