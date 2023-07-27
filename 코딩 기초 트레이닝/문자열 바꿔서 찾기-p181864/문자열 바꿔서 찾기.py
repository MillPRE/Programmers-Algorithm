# https://school.programmers.co.kr/learn/courses/30/lessons/181864

def solution(myString, pat):
    myString = list(myString)
    change = []

    for s in myString:
        if s == 'A':
            change.append('B')
        else:
            change.append('A')

    return 1 if pat in ''.join(change) else 0


