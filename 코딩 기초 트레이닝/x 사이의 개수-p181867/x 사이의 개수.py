# https://school.programmers.co.kr/learn/courses/30/lessons/181867

def solution(myString):
    answer = []
    lens = 0

    for s in myString:
        if s != 'x':
            lens += 1
        else:
            answer.append(lens)
            lens = 0

    answer.append(lens)
    return answer
