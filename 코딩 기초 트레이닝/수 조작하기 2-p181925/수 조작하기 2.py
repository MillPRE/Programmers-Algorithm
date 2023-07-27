# https://school.programmers.co.kr/learn/courses/30/lessons/181925

def solution(numLog):
    answer = ''
    prev = numLog[0]

    for next in range(len(numLog)-1):
        next = next+1

        diff = abs(numLog[next] - prev)
        if numLog[next] > prev:
            if diff == 1:
                answer += 'w'
            else:
                answer += 'd'
        else:
            if diff == 1:
                answer += 's'
            else:
                answer += 'a'

        prev = numLog[next]

    return answer
