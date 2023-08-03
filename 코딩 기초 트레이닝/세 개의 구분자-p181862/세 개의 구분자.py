# https://school.programmers.co.kr/learn/courses/30/lessons/181862

def solution(myStr):
    answer = []
    sub = ''

    myStr = list(myStr)
    for s in myStr:
        if not s in ['a', 'b', 'c']:
            sub += s
        elif len(sub) > 0:
            answer.append(sub)
            sub = ''

    if len(sub) > 0 :
        answer.append(sub)

    return ['EMPTY'] if len(answer) == 0 else answer
