def dijkstra():
    INF = float('inf')
    # start에서 특정 도시까지 가는데 걸리는 최소한의 비용
    cost = [INF for _ in range(N+1)]
    # 방문 여부
    visited = [False for _ in range(N+1)]
    cost[start] = 0

    # 모든 노드에 대해서
    for _ in range(N+1):
        min_cost = INF
        # 방문하지 않은 도시 중 비용이 최소로 걸리는 도시를 찾아서
        for i in range(N+1):
            if not visited[i] and min_cost > cost[i]:
                min_cost = cost[i]
                idx = i  # 인덱스 저장

        visited[idx] = True

        for j in range(N+1):
            # 갈 수 있고, 그 도시를 거쳐 가는 것이 더 싸다면 최소 비용 교체
            if cities[idx][j] and cost[idx] + cities[idx][j] < cost[j]:
                cost[j] = cost[idx] + cities[idx][j]

    return cost[end]


N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수

cities = [[0] * (N+1) for _ in range(N+1)]  # 도시 간 비용을 나타내는 2차원 리스트

# 버스정보: 시작지, 도착지, 요금 입력
for i in range(M):
    s, e, c = map(int, input().split())
    cities[s][e] = c

start, end = map(int, input().split())  # 출발점, 도착점

answer = dijkstra()

print(answer)