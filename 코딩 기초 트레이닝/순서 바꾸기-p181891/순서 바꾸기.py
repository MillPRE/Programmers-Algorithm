# https://school.programmers.co.kr/learn/courses/30/lessons/181891

def solution(num_list, n):
    left = num_list[:n]
    right = num_list[n:]

    return right + left
