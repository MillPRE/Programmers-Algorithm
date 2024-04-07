def solution(arr):
    answer = []
    idx = 1
    target = arr[0]
    while idx < len(arr):
        if arr[idx] != target:
            answer.append(target)
            target = arr[idx]

        if idx == len(arr) - 1:
            answer.append(target)
        idx += 1

    return answer