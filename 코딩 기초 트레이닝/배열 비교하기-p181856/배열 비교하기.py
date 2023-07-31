# https://school.programmers.co.kr/learn/courses/30/lessons/181856

def solution(arr1, arr2):
    # arr2 -1
    # arr1 1
    # == 0

    if len(arr1) == len(arr2):
        if sum(arr1) == sum(arr2):
            return 0
        else:
            return 1 if sum(arr1) > sum(arr2) else -1
    else:
        return 1 if len(arr1) > len(arr2) else -1
