# https://school.programmers.co.kr/learn/courses/30/lessons/181898

def solution(arr, idx):
    tmp = arr[idx:]
    if 1 in tmp:
        return arr.index(1, idx, )
    else:
        return -1
