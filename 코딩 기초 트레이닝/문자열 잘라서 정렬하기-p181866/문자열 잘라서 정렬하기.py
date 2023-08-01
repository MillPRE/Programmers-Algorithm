# https://school.programmers.co.kr/learn/courses/30/lessons/181866

def solution(myString):
    answer = []

    current = ''


    for d in list(myString):
        if d == 'x':
            if len(current) != 0:
                answer.append(current)
                current = ''
        else:
            current += d


    if len(current) > 0:
        answer.append(current)

    answer.sort()

    return answer
