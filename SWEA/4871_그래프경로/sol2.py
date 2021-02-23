import sys
sys.stdin = open('sample_input.txt')

def solution(V, E, graph, S, G):
    # vertex No == visited idx == graph idx
    visited = [False for _ in range(V+1)]
    to_visits = [S]
    # path = []

    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = True
            # path.append(current)
            to_visits += graph[current]
    # print(path)
    return int(visited[G])



T = int(input())

for tc in range(1, T+1):
    # Vertex, Edge 의 개수
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, solution(V, E, graph, S, G)))


