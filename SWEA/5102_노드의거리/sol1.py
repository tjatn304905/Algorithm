import sys
sys.stdin = open('sample_input.txt')

def solution(V, edges, S, G):
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    stack = [[S, 0]]

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    while stack:
        if stack[0][0] == G:
            return stack[0][1]
        current = stack.pop(0)
        if not visited[current[0]]:
            visited[current[0]] = 1
            for i in graph[current[0]]:
                if not visited[i]:
                    stack.append([i, current[1] + 1])
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        edges.append(list(map(int, input().split())))
    S, G = map(int, input().split())

    print('#{} {}'.format(tc, solution(V, edges, S, G)))