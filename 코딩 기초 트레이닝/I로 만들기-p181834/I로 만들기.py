# https://school.programmers.co.kr/learn/courses/30/lessons/181834

def solution(myString):
    ASCII_I = 108
    answer = ''

    myString = list(myString)

    for m in myString:
        if ord(m) < ASCII_I:
            answer += 'l'
        else:
            answer += m

    return answer
