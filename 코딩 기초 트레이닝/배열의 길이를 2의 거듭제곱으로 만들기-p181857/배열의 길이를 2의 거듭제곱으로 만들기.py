# https://school.programmers.co.kr/learn/courses/30/lessons/181857

def solution(arr):
    lens = len(arr)

    if(lens & (lens-1) == 0):
        return arr
    else:
        while(lens & (lens-1) != 0):
            arr.append(0)
            lens = len(arr)
    return arr
