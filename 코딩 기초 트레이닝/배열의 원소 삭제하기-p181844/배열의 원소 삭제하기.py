# https://school.programmers.co.kr/learn/courses/30/lessons/181844

def solution(arr, delete_list):
    answer = []

    for a in arr:
        if a not in delete_list:
            answer.append(a)

    return answer
