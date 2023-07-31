# https://school.programmers.co.kr/learn/courses/30/lessons/181887

def solution(num_list):
    answer = [0,0]

    for index, num in enumerate(num_list):
        if (index+1) % 2 == 0:
            answer[0] += num
        else:
            answer[1] += num

    return answer[0] if answer[0] >= answer[1] else answer[1]
