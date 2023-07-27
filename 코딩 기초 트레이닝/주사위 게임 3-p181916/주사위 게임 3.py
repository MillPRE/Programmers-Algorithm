# https://school.programmers.co.kr/learn/courses/30/lessons/181916

def solution(a, b, c, d):
    arr = [a,b,c,d]
    answer = 0
    # 4 all p - 1111 * p
    # 3 p 1 q - (10 * p + q)**2
    # 2p 2q - (p+q) * |p-q|(abs)
    # 2p 1q 1r - q*r
    # all different - 가장 작은 숫자

    dic = {key : 0 for key in arr}
    _keys = list(dic.keys())

    for a in arr:
        dic[a] += 1

    _set = set(arr)

    if len(_set) == 1:
        return 1111 * a
    elif len(_set) == 2:


        if dic[_keys[0]] != dic[_keys[1]] :
            # 3p 1q
            p = _keys[0] if dic[_keys[0]] > dic[_keys[1]] else _keys[1]
            q = _keys[1] if dic[_keys[0]] > dic[_keys[1]] else _keys[0]

            return (10 * p + q)**2
        else:
            # 2p 2q
            p = _keys[0] if _keys[0] >= _keys[1] else _keys[1]
            q = _keys[1] if _keys[0] >= _keys[1] else _keys[0]
            return (p + q) * abs(p - q)
    elif len(_set) == 3:
        qr = []
        for k in _keys:
            if dic[k] == 1:
                qr.append(k)
        return qr[0] * qr[1]
    else:
        return min(arr)
