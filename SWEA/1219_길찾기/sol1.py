import sys
sys.stdin = open('input.txt')

def solution(edges, graph):
    visited = [0 for _ in range(100)]
    stack = [0]

    while stack:
        current = stack.pop()
        if current == 99:
            return 1
        if not visited[current]:
            visited[current] = 1
            stack += graph[current]
    return 0

T = 10

for tc in range(1, T+1):
    tc, edges = map(int, input().split())

    edge = list(map(int, input().split()))

    graph = [[] for _ in range(100)]

    for i in range(edges*2):
        if not i % 2:
            idx = edge[i]
        else:
            graph[idx].append(edge[i])

    print('#{} {}'.format(tc, solution(edges, graph)))