# https://school.programmers.co.kr/learn/courses/30/lessons/181908

def solution(my_string, is_suffix):
    if is_suffix in my_string:
        if len(my_string) - len(is_suffix) == my_string.rfind(is_suffix):
            return 1
        else:
            return 0
    else:
        return 0
