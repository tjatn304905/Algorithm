import sys
sys.stdin = open('sample_input.txt')

def solution(V, graph, S, G):
    visited = [0 for _ in range(V+1)]
    stack = [S]

    # stack이 남아있을 때까지
    while stack:
        # 스택에 남아 있는 곳의 끝부분부터 탐색
        current = stack.pop()
        # 방문한 적이 없으면
        if not visited[current]:
            # 방문 표시를 하고
            visited[current] = 1
            # 스택에 current에서 갈 수 있는 곳을 추가
            # 추가되지 않았다면 stack에 남은 나머지 node를 current로 받게 될 것임.
            stack += graph[current]
    # G가 방문 되었는지를 리턴
    return(visited[G])


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
    S, G = map(int, input().split())

    print('#{} {}'.format(tc, solution(V, graph, S, G)))
