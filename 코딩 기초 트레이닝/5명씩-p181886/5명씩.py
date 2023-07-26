# https://school.programmers.co.kr/learn/courses/30/lessons/181886

def solution(names):
    answer = []

    temp = []
    for name in names:
        temp.append(name)

        if len(temp) == 5:
            answer.append(temp[0])
            temp.clear()

    if len(temp) != 0:
        answer.append(temp[0])

    return answer
