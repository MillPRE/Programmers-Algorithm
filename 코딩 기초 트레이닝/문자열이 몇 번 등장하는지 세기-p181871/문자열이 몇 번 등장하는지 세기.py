# https://school.programmers.co.kr/learn/courses/30/lessons/181871

def solution(myString, pat):
    answer = 0

    for i in range(len(myString) - len(pat) +1):
        if myString[i: i+len(pat)] == pat:
            answer += 1


    return answer
