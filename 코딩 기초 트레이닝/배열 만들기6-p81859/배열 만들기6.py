# https://school.programmers.co.kr/learn/courses/30/lessons/181859

def solution(arr):
    answer = []
    i = 0

    while i < len(arr) :
        if len(answer) == 0:
            answer.append(arr[i])
            i += 1
        elif len(answer) > 0 and answer[len(answer)-1] == arr[i]:
            del answer[len(answer)-1]
            i += 1
        elif len(answer) > 0 and answer[len(answer)-1] != arr[i]:
            answer.append(arr[i])
            i += 1

    return [-1] if len(answer) == 0 else answer
