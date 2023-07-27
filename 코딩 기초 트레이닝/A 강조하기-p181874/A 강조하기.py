# https://school.programmers.co.kr/learn/courses/30/lessons/181874

def solution(myString):
    answer = ''
    myString = list(myString)

    for m in myString:
        if m == 'a' or m == 'A':
            answer += 'A'
        else:
            answer += m.lower()

    return answer
