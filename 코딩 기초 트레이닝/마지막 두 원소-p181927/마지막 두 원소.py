def solution(num_list):
    length = len(num_list)

    # a: 마지막 전
    # b: 마지막

    a = num_list[length-2]
    b = num_list[length-1]
    num_list.append(b*2 if b <= a else b - a)

    return num_list
