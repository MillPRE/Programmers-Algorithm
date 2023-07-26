def solution(rny_string):
    answer = []

    for d in rny_string:
        if d == 'm':
            answer.append('rn')
        else :
            answer.append(d)

    return ''.join(answer)
