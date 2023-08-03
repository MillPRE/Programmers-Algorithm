# https://school.programmers.co.kr/learn/courses/30/lessons/181897

def solution(n, slicer, num_list):
    # n == 1 0 ~ b
    # n == 2 a ~
    # n == 3 a ~ b
    # n == 4 a ~ b c 간격

    if n == 1:
        b = slicer[1]
        return num_list[0: b+1]
    elif n == 2:
        a = slicer[0]
        return num_list[a:]
    elif n == 3:
        a = slicer[0]
        b = slicer[1]
        return num_list[a: b+1]
    else:
        a = slicer[0]
        b = slicer[1]
        c = slicer[2]
        return num_list[a:b+1:c]
