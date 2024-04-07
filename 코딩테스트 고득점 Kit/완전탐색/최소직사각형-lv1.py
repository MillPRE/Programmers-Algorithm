# w에 작은 값들, h에 큰 값들
def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp
    w = [s[0] for s in sizes]
    h = [s[1] for s in sizes]
    return  max(w) * max(h)