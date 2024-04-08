# 크루스칼 알고리즘 사용해야 함.
# 최소 비용으로 모든 노드 연결 문제

def find(parent, x):
    if parent[x] == x:
        return x

    return find(parent, parent[x])

def union(parent, x, y):
    x_root, y_root = find(parent, x), find(parent, y)
    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root
    return parent
def solution(n, costs):
    answer = 0

    print(costs)
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]

    for c in costs:
        v1, v2, cost = c
        if find(parent, v1) != find(parent, v2):
            answer += cost
            parent = union(parent, v1, v2)
    return answer

ns = [
    4
]

costs = [
    [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
]

results = [
    4
]

for idx in range(len(costs)):
    print(f'test_case #{idx}: {costs[idx]}')
    cost = costs[idx]
    n = ns[idx]
    answer = solution(n, cost)
    print(f'return answer: {answer}, real_answer: {results[idx]}')
    print(f'{"PASS" if answer == results[idx] else "FAIL"}\n')