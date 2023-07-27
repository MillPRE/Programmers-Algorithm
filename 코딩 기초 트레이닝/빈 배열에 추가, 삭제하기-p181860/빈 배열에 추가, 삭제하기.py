# https://school.programmers.co.kr/learn/courses/30/lessons/181860

def solution(arr, flag):
    answer = []

    for index, f in enumerate(flag):
        if(f):
            a = [ arr[index] for a in range(arr[index] * 2)]
            answer += a
        else:
            answer = answer[0: len(answer) - arr[index]]

    return answer
