# dfs
def dfs(graph, V):
    visited = [0 for _ in range(len(graph))]
    stack = [V]
    trace = []

    for i in range(len(graph)):
        graph[i] = sorted(graph[i])[::-1]

    # stack이 남아있을 때까지
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = 1
            stack += graph[current]
            # trace 기록하기
            trace.append(current)
    return trace


# bfs
def bfs(graph, V):
    visited = [0 for _ in range(len(graph))]
    queue = [V]
    trace = []

    for i in range(len(graph)):
        graph[i] = sorted(graph[i])

    while queue:
        current = queue.pop(0)
        if not visited[current]:
            visited[current] = 1
            trace.append(current)
        for i in graph[current]:
            if not visited[i]:
                queue.append(i)
    return trace


N, M, V = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]

for line in lines:
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])

print(*dfs(graph, V))
print(*bfs(graph, V))
